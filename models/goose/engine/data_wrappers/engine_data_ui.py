import pygame
import math
import datetime
from models.goose.engine.data_wrappers.earth_data import get_planet_data

# === CONFIG ===
WIDTH, HEIGHT = 1000, 1000
CENTER = WIDTH // 2, HEIGHT // 2
FPS = 60
FONT_SIZE = 18

SIM_SPEED_OPTIONS = [1, 30, 365, 3650]  # days/sec
DEFAULT_SPEED = SIM_SPEED_OPTIONS[1]

# Visuals
SUN_SIZE = 24
EARTH_SIZE = 14
MOON_SIZE = 6
MOON_ORBIT_SCALE = 60
EARTH_ORBIT_COLOR = (50, 50, 100)
MOON_ORBIT_COLOR = (80, 80, 80)
SLIDER_COLOR_ACTIVE = (100, 100, 255)
SLIDER_COLOR_INACTIVE = (180, 180, 180)


def solar_data_ui(solar_data: dict, start_date: datetime.datetime, end_date: datetime.datetime):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Solar System UI: Earth & Moon Orbits")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", FONT_SIZE)

    scale = (min(WIDTH, HEIGHT) // 2 - 100) / solar_data["bodies"]["Earth"]["radius"]

    earth_radius_px_visual = int(solar_data["bodies"]["Earth"]["radius"] * scale)
    moon_radius_px_visual = MOON_ORBIT_SCALE

    slider_buttons = []
    slider_start_x = 200
    slider_y = 20
    for i, speed in enumerate(SIM_SPEED_OPTIONS):
        rect = pygame.Rect(slider_start_x + i * 60, slider_y, 50, 24)
        slider_buttons.append((speed, rect))

    sim_time = start_date
    sim_speed = DEFAULT_SPEED
    running = True

    while running:
        screen.fill((0, 0, 0))
        days_advanced = sim_speed * (1 / FPS)
        sim_time += datetime.timedelta(days=days_advanced)
        years_since_start = (sim_time - start_date).days / 365.25

        if pygame.time.get_ticks() % 10000 < 50:
            solar_data["earth_data"] = solar_data["refresh_earth_data"]()

        earth_data = solar_data["earth_data"]
        pressure = earth_data['weather']['pressure']
        orbit_modifier = (1040 - pressure) / 60 + 1.0

        (earth_x, earth_y), (moon_x, moon_y) = compute_positions(
            solar_data, years_since_start, orbit_modifier, scale
        )

        draw_system(
            screen, solar_data, earth_x, earth_y, moon_x, moon_y,
            earth_radius_px_visual, moon_radius_px_visual, font, sim_time,
            sim_speed, slider_buttons, slider_start_x, slider_y
        )

        sim_time += datetime.timedelta(days=days_advanced)
        if sim_time > end_date:
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for speed, rect in slider_buttons:
                    if rect.collidepoint(event.pos):
                        sim_speed = speed

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


def compute_positions(solar_data, years_since_start, orbit_modifier, scale):
    earth_angle = 2 * math.pi * (years_since_start % 1)
    earth_radius_px = int(solar_data["bodies"]["Earth"]["radius"] * scale * orbit_modifier)
    earth_x = CENTER[0] + int(earth_radius_px * math.cos(earth_angle))
    earth_y = CENTER[1] + int(earth_radius_px * math.sin(earth_angle))

    moon_angle = 2 * math.pi * ((years_since_start * 13.37) % 1)
    moon_radius_px = int(MOON_ORBIT_SCALE * orbit_modifier)
    moon_x = earth_x + int(moon_radius_px * math.cos(moon_angle))
    moon_y = earth_y + int(moon_radius_px * math.sin(moon_angle))

    return (earth_x, earth_y), (moon_x, moon_y)


def draw_system(screen, solar_data, earth_x, earth_y, moon_x, moon_y,
                 earth_orbit_radius, moon_orbit_radius, font, sim_time,
                 current_speed, slider_buttons, slider_start_x, slider_y):

    pygame.draw.circle(screen, solar_data["colors"]["Sun"], CENTER, SUN_SIZE)
    pygame.draw.circle(screen, EARTH_ORBIT_COLOR, CENTER, earth_orbit_radius, width=1)
    pygame.draw.circle(screen, MOON_ORBIT_COLOR, (earth_x, earth_y), moon_orbit_radius, width=1)
    pygame.draw.circle(screen, solar_data["colors"]["Earth"], (earth_x, earth_y), EARTH_SIZE)
    pygame.draw.circle(screen, solar_data["colors"]["Moon"], (moon_x, moon_y), MOON_SIZE)

    date_text = font.render(f"Earth Date: {sim_time}", True, (255, 255, 255))
    screen.blit(date_text, (20, 20))

    # label = font.render("Speed (days/sec):", True, (255, 255, 255))
    # screen.blit(label, (slider_start_x - 150, slider_y + 2))
    # for speed, rect in slider_buttons:
    #     color = SLIDER_COLOR_ACTIVE if speed == current_speed else SLIDER_COLOR_INACTIVE
    #     pygame.draw.rect(screen, color, rect)
    #     label = font.render(str(speed), True, (0, 0, 0))
    #     screen.blit(label, label.get_rect(center=rect.center))
