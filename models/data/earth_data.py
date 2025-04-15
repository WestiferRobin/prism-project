import os
import datetime
from pathlib import Path

import fiona
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

from configs.earth_data_config import GPKG_FILE
from models.data.weather_data.v1_weather_data import fetch_climate_data
from models.ui.earth_map_ui import run_earth_map_ui


def fetch_city_data():
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
    return gpd.GeoDataFrame(city_df, geometry="geometry", crs="EPSG:4326")


def fetch_earth_data(start_date, end_date, is_ui=False):
    # Define save path
    output_dir = Path(GPKG_FILE).parent
    output_file = output_dir / f"earth_climate_data_{start_date.date()}_{end_date.date()}.csv"

    # ✅ If file exists, skip fetch
    if output_file.exists():
        print(f"📂 Loading existing climate data from: {output_file}")
        combined_df = pd.read_csv(output_file)
    else:
        print("🌍 Loading world map layers from GeoPackage...")
        try:
            layers = fiona.listlayers(str(GPKG_FILE))
            print("Available Layers:", layers)
        except Exception as e:
            print(f"❌ Failed to list GPKG layers: {e}")
            return None

        try:
            earth_data = gpd.read_file(GPKG_FILE, layer="ne_110m_admin_0_countries")
        except Exception as e:
            print(f"❌ Failed to read GeoPackage: {e}")
            return None

        centroids = earth_data.to_crs("EPSG:3395").copy()
        centroids["latitude"] = centroids.centroid.to_crs("EPSG:4326").y
        centroids["longitude"] = centroids.centroid.to_crs("EPSG:4326").x

        combined_records = []

        print("📡 Fetching climate data for each country centroid...")
        count = 0
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

            combined_records.append(climate_df)
            count += 1
            print(f"{count} / {len(centroids)} countries processed")

        if not combined_records:
            print("⚠️ No climate data was fetched.")
            return None

        combined_df = pd.concat(combined_records, ignore_index=True)
        print("✅ Combined Earth + Climate data loaded.")

        # ✅ Save result
        combined_df.to_csv(output_file, index=False)
        print(f"📁 Saved to: {output_file}")

    # ✅ If UI is enabled, visualize it
    if is_ui:
        run_earth_map_ui(combined_df, start_date, end_date)

    return combined_df
