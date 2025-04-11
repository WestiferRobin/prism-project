import datetime
import pygame
import pandas as pd

from configs.goose_config import WIDTH, HEIGHT, FONT_SIZE, DEFAULT_SPEED, FPS, CENTER, SUN_SIZE, SUN_COLOR

# === Planet Visual Configuration ===
PLANET_CONFIG = {
    "mercury": {"color": (169, 169, 169), "size": 3},
    "venus":   {"color": (255, 165, 0),   "size": 5},
    "earth":   {"color": (0, 102, 255),   "size": 9},
    "mars":    {"color": (255, 0, 0),     "size": 6},
    "jupiter": {"color": (200, 150, 100), "size": 11},
    "saturn":  {"color": (210, 180, 140), "size": 10},
    "uranus":  {"color": (100, 200, 255), "size": 8},
    "neptune": {"color": (0, 0, 139),     "size": 8},
    "moon":    {"color": (200, 200, 200), "size": 3},
}

planet_trails = {name: [] for name in PLANET_CONFIG.keys()}

# === UI Main Loop ===
def run_solar_system_ui(start_date: datetime.datetime, end_date: datetime.datetime):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Solar System Orbits - Real Ephemeris")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", FONT_SIZE)

    offset = pygame.Vector2(0, 0)
    zoom = 1.0
    zoom_speed = 0.01
    pan_speed = 20
    sim_time = start_date
    sim_speed = DEFAULT_SPEED
    running = True

    # Load ephemeris data
    EPHEMERIS_PATH = f"data/solar_data/solar_data_{start_date.date()}_{end_date.date()}.csv"
    df_ephemeris = pd.read_csv(EPHEMERIS_PATH)
    df_ephemeris["date"] = pd.to_datetime(df_ephemeris["date"])
    df_ephemeris.set_index("date", inplace=True)

    # === Main Event Loop ===
    while running:
        screen.fill((0, 0, 0))

        # Input Handling
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: offset.y += pan_speed
        if keys[pygame.K_s]: offset.y -= pan_speed
        if keys[pygame.K_a]: offset.x += pan_speed
        if keys[pygame.K_d]: offset.x -= pan_speed
        if keys[pygame.K_EQUALS] or keys[pygame.K_KP_PLUS]: zoom *= (1 + zoom_speed)
        if keys[pygame.K_MINUS] or keys[pygame.K_KP_MINUS]: zoom /= (1 + zoom_speed)

        # Time progression
        days_advanced = sim_speed * (1 / FPS)
        sim_time += datetime.timedelta(days=days_advanced)

        draw_solar_system(df_ephemeris, screen, sim_time, offset, font, zoom)
        draw_speed_slider(screen, sim_speed, font)

        if sim_time > end_date:
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if WIDTH - 160 <= x <= WIDTH - 20 and 20 <= y <= 40:
                    sim_speed = ((x - (WIDTH - 160)) / 140) * 100  # 0 to 100 scale

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

# === Draw Planets ===
def draw_solar_system(df_ephemeris, screen, sim_time, offset, font, zoom):
    try:
        data = df_ephemeris.loc[pd.Timestamp(sim_time.date())]
    except KeyError:
        return

    AU_TO_PX = (min(WIDTH, HEIGHT) // 2 - 100) * zoom
    scale = AU_TO_PX

    pygame.draw.circle(screen, SUN_COLOR, CENTER + offset, max(5, int(SUN_SIZE * zoom)))

    earth_x = earth_y = None

    for name in PLANET_CONFIG:
        x_key = f"{name}_x"
        y_key = f"{name}_y"
        if x_key not in data or y_key not in data:
            continue

        if name == "moon":
            if earth_x is None or earth_y is None:
                continue
            body_x = int(earth_x + data[x_key] * scale * 25)
            body_y = int(earth_y + data[y_key] * scale * 25)
        else:
            body_x = int(CENTER[0] + offset.x + data[x_key] * scale)
            body_y = int(CENTER[1] + offset.y + data[y_key] * scale)
            if name == "earth":
                earth_x, earth_y = body_x, body_y

        planet_trails[name].append((body_x, body_y))
        for pt in planet_trails[name][-300:]:
            pygame.draw.circle(screen, PLANET_CONFIG[name]['color'], pt, 1)

        pygame.draw.circle(
            screen,
            PLANET_CONFIG[name]['color'],
            (body_x, body_y),
            max(2, int(PLANET_CONFIG[name]['size'] * zoom))
        )

    date_text = font.render(f"Earth Date: {sim_time.date()}", True, (255, 255, 255))
    screen.blit(date_text, (20, 20))

# === Speed Slider ===
def draw_speed_slider(screen, sim_speed, font):
    bar_x = WIDTH - 160
    bar_y = 20
    bar_width = 140
    bar_height = 20
    fill_width = int((sim_speed / 100) * bar_width)

    pygame.draw.rect(screen, (100, 100, 100), (bar_x, bar_y, bar_width, bar_height))
    pygame.draw.rect(screen, (0, 200, 0), (bar_x, bar_y, fill_width, bar_height))

    speed_text = font.render(f"Speed: {sim_speed:.1f}d/s", True, (255, 255, 255))
    screen.blit(speed_text, (bar_x, bar_y - 22))
