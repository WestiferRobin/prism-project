import os

import fiona
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

from models.data.weather_data.v1_weather_data import fetch_climate_data
from models.ui.earth_map_ui import run_earth_map_ui

# Path to your downloaded GeoPackage file
GPKG_FILE = "D:/Dev/nexus-framework/data/earth_data/natural_earth_vector.gpkg"


def fetch_earth_data(start_date, end_date):
    print("Loading world map...")
    layers = fiona.listlayers(GPKG_FILE)
    print("Available Layers:", layers)

    # Load countries from the geopackage
    earth_data = gpd.read_file(GPKG_FILE, layer="ne_110m_admin_0_countries")

    # Select representative cities or country centroids
    centroids = earth_data.to_crs("EPSG:3395").copy()
    centroids["latitude"] = centroids.centroid.to_crs("EPSG:4326").y
    centroids["longitude"] = centroids.centroid.to_crs("EPSG:4326").x

    combined_records = []

    print("Fetching climate data for each country centroid...")
    for _, row in centroids.iterrows():
        lat = row["latitude"]
        lon = row["longitude"]
        country = row["NAME"]

        climate_df = fetch_climate_data(lat, lon, start_date, end_date)
        if climate_df.empty:
            continue

        climate_df["country"] = country
        climate_df["latitude"] = lat
        climate_df["longitude"] = lon
        if len(combined_records) > 10:
            break
        combined_records.append(climate_df)

    if not combined_records:
        print("⚠️ No climate data was fetched.")
        return None

    combined_df = pd.concat(combined_records, ignore_index=True)
    print("✅ Combined Earth + Climate data loaded.")

    return combined_df


def fetch_city_data():
    # Sample city coordinates (latitude, longitude) => Look at calculating top 25 GDP per year for countries and cities
    cities = {
        "New York": (40.7128, -74.0060),
        "London": (51.5074, -0.1278),
        "Tokyo": (35.6895, 139.6917),
        "Sydney": (-33.8688, 151.2093),
        "Cairo": (30.0444, 31.2357),
        "São Paulo": (-23.5505, -46.6333),
    }

    city_df = pd.DataFrame([
        {"city": name, "geometry": Point(lon, lat)} for name, (lat, lon) in cities.items()
    ])
    city_gdf = gpd.GeoDataFrame(city_df, geometry="geometry", crs="EPSG:4326")

    return city_gdf


if __name__ == "__main__":

    start_time = "2025-04-01"
    end_time = "2025-04-02"

    earth_data = fetch_earth_data(start_time, end_time)
    city_data = fetch_city_data()

    run_earth_map_ui(earth_data, city_data)
