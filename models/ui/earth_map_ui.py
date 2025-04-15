import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd


def run_earth_map_ui(earth_data, city_data):
    print("🌍 Rendering Earth Data UI...")

    # Convert Earth climate data to GeoDataFrame
    geo_df = gpd.GeoDataFrame(
        earth_data,
        geometry=gpd.points_from_xy(earth_data["longitude"], earth_data["latitude"]),
        crs="EPSG:4326"
    )

    # Setup the figure
    fig, ax = plt.subplots(figsize=(15, 8))
    world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
    world.plot(ax=ax, edgecolor="gray", facecolor="white")

    # Plot countries with temperature shading
    avg_temp = geo_df.groupby("country")["temperature_2m_max"].mean()
    geo_df["avg_temp"] = geo_df["country"].map(avg_temp)

    # Normalize temperature to color scale
    geo_df.plot(ax=ax, column="avg_temp", cmap="YlOrRd", legend=True, markersize=20)

    # Plot cities
    city_data.plot(ax=ax, color="black", markersize=40, label="Cities")

    # Annotate city names
    for _, row in city_data.iterrows():
        ax.text(row.geometry.x + 1.5, row.geometry.y, row["city"], fontsize=9, color="black")

    ax.set_title("🌡️ Climate Overview with Major Cities", fontsize=18)
    plt.axis("off")
    plt.tight_layout()
    plt.legend()
    plt.show()
