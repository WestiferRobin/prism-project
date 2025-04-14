import fiona
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point


def load_weather_data(start_date, end_date):
    print(f"WEATHER DATA FOR {start_date} - {end_date}")


# Path to your downloaded GeoPackage file
GPKG_FILE = "data/earth_data/natural_earth_vector.gpkg"


def load_earth_data():
    # List all layers in the GPKG
    layers = fiona.listlayers(GPKG_FILE)
    print("Available Layers:", layers)

    # Load world map (countries layer)
    world = gpd.read_file(GPKG_FILE, layer="ne_110m_admin_0_countries")

    return world


def load_city_data():
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





