import datetime
import math
import pygame

from configs.goose_config import WIDTH, HEIGHT, FONT_SIZE, DEFAULT_SPEED, FPS, CENTER, SUN_SIZE

G = 4 * math.pi ** 2  # AU^3 / (yr^2 * solar_mass), simplified gravitational constant
SUN_MASS = 1.0  # In solar masses

# Sizes in km (converted to AU)
EARTH_RADIUS_AU = 6371 / 1.496e+8
MOON_RADIUS_AU = 1737 / 1.496e+8
SUN_RADIUS_AU = 695700 / 1.496e+8

PLANETS = {
    "Mercury": {"radius": 0.39, "period": 0.24, "mass": 0.055, "color": (169, 169, 169), "size": 5},
    "Venus":   {"radius": 0.72, "period": 0.62, "mass": 0.815, "color": (255, 165, 0),   "size": 7},
    "Earth":   {"radius": 1.00, "period": 1.00, "mass": 1.0, "color": (0, 102, 255),    "size": 9},
    "Mars":    {"radius": 1.52, "period": 1.88, "mass": 0.107, "color": (255, 0, 0),      "size": 6},
}

MOONS = {
    "Earth": [{"distance_ratio": 0.00257, "period": 0.0748, "size": 3, "color": (200, 200, 200)}],
    "Mars": [
        {"distance_ratio": 0.0005, "period": 0.319, "size": 2, "color": (150, 150, 150)},
        {"distance_ratio": 0.0009, "period": 1.263, "size": 2, "color": (130, 130, 130)}
    ]
}

def run_solar_system_ui(start_date: datetime.datetime, end_date: datetime.datetime):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Solar System Orbits")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", FONT_SIZE)

    max_au = max(p["radius"] for p in PLANETS.values())
    base_scale = (min(WIDTH, HEIGHT) // 2 - 100) / max_au
    zoom = 1.0
    offset = pygame.Vector2(0, 0)
    pan_speed = 20

    sim_time = start_date
    sim_speed = DEFAULT_SPEED
    running = True

    while running:
        screen.fill((0, 0, 0))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: offset.y += pan_speed
        if keys[pygame.K_s]: offset.y -= pan_speed
        if keys[pygame.K_a]: offset.x += pan_speed
        if keys[pygame.K_d]: offset.x -= pan_speed
        if keys[pygame.K_EQUALS] or keys[pygame.K_KP_PLUS]: zoom *= 1.01
        if keys[pygame.K_MINUS] or keys[pygame.K_KP_MINUS]: zoom /= 1.01

        days_advanced = sim_speed * (1 / FPS)
        sim_time += datetime.timedelta(days=days_advanced)
        years_since_start = (sim_time - start_date).days / 365.25

        draw_solar_system(screen, years_since_start, base_scale * zoom, offset, font, sim_time, zoom)

        if sim_time > end_date:
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

def draw_solar_system(screen, years_since_start, scale, offset, font, sim_time, zoom):
    pygame.draw.circle(screen, (255, 255, 0), CENTER + offset, max(5, int(SUN_SIZE * zoom)))

    for name, planet in PLANETS.items():
        a = planet["radius"]
        T = math.sqrt(a**3 / SUN_MASS)
        angle = 2 * math.pi * (years_since_start / T % 1)
        orbit_radius_px = int(a * scale)

        x = CENTER[0] + offset.x + int(orbit_radius_px * math.cos(angle))
        y = CENTER[1] + offset.y + int(orbit_radius_px * math.sin(angle))

        pygame.draw.circle(screen, (60, 60, 100), CENTER + offset, orbit_radius_px, width=1)
        pygame.draw.circle(screen, planet["color"], (x, y), max(2, int(planet["size"] * zoom)))

        for moon in MOONS.get(name, []):
            m_a = moon["distance_ratio"] * a
            m_T = moon["period"]
            m_angle = 2 * math.pi * (years_since_start / m_T % 1)
            moon_orbit_radius = int(m_a * scale * 100)  # exaggerate moon orbit for visibility

            mx = x + int(moon_orbit_radius * math.cos(m_angle))
            my = y + int(moon_orbit_radius * math.sin(m_angle))

            pygame.draw.circle(screen, (100, 100, 100), (x, y), moon_orbit_radius, width=1)
            pygame.draw.circle(screen, moon["color"], (mx, my), max(1, int(moon["size"] * zoom)))

    date_text = font.render(f"Earth Date: {sim_time.date()}", True, (255, 255, 255))
    screen.blit(date_text, (20, 20))
