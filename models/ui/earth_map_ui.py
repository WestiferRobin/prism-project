import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
import pygame

from configs.earth_data_config import GPKG_FILE
import pygame
import pandas as pd
from datetime import timedelta

WIDTH, HEIGHT = 1200, 600

def latlon_to_xy(lat, lon):
    x = int((lon + 180) * (WIDTH / 360))
    y = int((90 - lat) * (HEIGHT / 180))
    return x, y

def get_temp_color(temp):
    if pd.isna(temp):
        return (100, 100, 100)

    t = max(min(temp, 40), -20)
    norm = (t + 20) / 60.0

    if norm < 0.5:
        r = int(norm * 2 * 255)
        g = int(norm * 2 * 255)
        b = 255
    else:
        r = 255
        g = int((1 - norm) * 2 * 255)
        b = 0

    return (r, g, b)

def run_earth_map_ui(earth_data: pd.DataFrame, start_date, end_date, days_per_second=60):
    print(f"🕹️ Simulating Earth Climate from {start_date.date()} → {end_date.date()} at {days_per_second} days/sec")

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("🌍 Earth Climate Heatmap")

    font = pygame.font.SysFont(None, 28)
    label_font = pygame.font.SysFont(None, 24)

    clock = pygame.time.Clock()
    day_index = 0
    total_days = (end_date - start_date).days + 1
    running = True

    while running:
        screen.fill((20, 20, 30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        curr_date = start_date + timedelta(days=day_index)
        frame_data = earth_data  # (Optional: replace with date-filtered data)

        for _, row in frame_data.iterrows():
            lat = row["latitude"]
            lon = row["longitude"]
            temp = row.get("temperature_2m_max", None)

            if pd.isna(temp):
                continue

            x, y = latlon_to_xy(lat, lon)
            color = get_temp_color(temp)
            pygame.draw.circle(screen, color, (x, y), 6)

        # UI labels
        screen.blit(label_font.render("🕒 Current Day:", True, (255, 255, 255)), (20, 20))
        screen.blit(font.render(str(curr_date.date()), True, (255, 255, 255)), (20, 45))

        pygame.display.flip()
        clock.tick(60)  # ⏱️ 60 FPS

        # ⏩ Simulate X days per frame
        day_index += days_per_second // 60  # simulate 60 days per second

        if day_index >= total_days:
            running = False

    pygame.quit()


def run_earth_plot_ui(earth_data: pd.DataFrame):
    print("🌍 Rendering Earth Data Plot UI...")

    # Build GeoDataFrame from coordinates
    geo_df = gpd.GeoDataFrame(
        earth_data,
        geometry=gpd.points_from_xy(earth_data["longitude"], earth_data["latitude"]),
        crs="EPSG:4326"
    )

    # Load country outlines
    world = gpd.read_file(GPKG_FILE, layer="ne_110m_admin_0_countries")

    # Compute average temperature per country
    avg_temp = geo_df.groupby("country")["temperature_2m_max"].mean()
    world["avg_temp"] = world["NAME"].map(avg_temp)

    # Plot map
    fig, ax = plt.subplots(figsize=(15, 8))
    world.plot(
        ax=ax,
        column="avg_temp",
        cmap="RdYlBu_r",
        legend=True,
        edgecolor="gray",
        missing_kwds={
            "color": "lightgray",
            "edgecolor": "white",
            "label": "No data"
        }
    )

    # Optionally plot centroids
    geo_df.plot(ax=ax, color="black", markersize=10, alpha=0.5, label="Centroids")

    ax.set_title("🌡️ Global Temperature Overview (Cold → Hot)", fontsize=18)
    plt.axis("off")
    plt.tight_layout()
    plt.legend()
    plt.show()
