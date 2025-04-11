
def load_weather_data(start_date, end_date):
    print(f"WEATHER DATA FOR {start_date} - {end_date}")

import fiona
import geopandas as gpd
import matplotlib.pyplot as plt

# Path to your downloaded GeoPackage file
GPKG_FILE = "../../data/earth_data/natural_earth_vector.gpkg"

# List all layers in the GPKG
layers = fiona.listlayers(GPKG_FILE)
print("Available Layers:", layers)

# Load world map (countries layer)
world = gpd.read_file(GPKG_FILE, layer="ne_110m_admin_0_countries")

# Sample city coordinates (latitude, longitude)
cities = {
    "New York": (40.7128, -74.0060),
    "London": (51.5074, -0.1278),
    "Tokyo": (35.6895, 139.6917),
    "Sydney": (-33.8688, 151.2093),
    "Cairo": (30.0444, 31.2357),
    "São Paulo": (-23.5505, -46.6333),
}

# Convert cities to a GeoDataFrame
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

city_df = pd.DataFrame([
    {"city": name, "geometry": Point(lon, lat)} for name, (lat, lon) in cities.items()
])
city_gdf = gpd.GeoDataFrame(city_df, geometry="geometry", crs="EPSG:4326")

# Plot the map with cities
fig, ax = plt.subplots()
world.plot(ax=ax, edgecolor="black", facecolor="lightgray")

# Plot cities as red dots
city_gdf.plot(ax=ax, color="red", markersize=50)

# Annotate city names
for idx, row in city_gdf.iterrows():
    ax.text(row.geometry.x + 2, row.geometry.y, row["city"], fontsize=9, color="darkred")

plt.title("World Map with Sample Cities", fontsize=16)
plt.axis("off")
plt.tight_layout()
plt.show()
