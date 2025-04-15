from io import StringIO

import requests
import pandas as pd
import datetime

from bs4 import BeautifulSoup
from skyfield.api import load
from skyfield import almanac
import geopandas as gpd
import fiona


def fetch_climate_data(latitude, longitude, start_date, end_date):
    url = (
        f"https://archive-api.open-meteo.com/v1/archive?latitude={latitude}&longitude={longitude}"
        f"&start_date={start_date.date()}&end_date={end_date.date()}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum"
        f"&timezone=UTC"
    )
    response = requests.get(url)
    data = response.json()
    return pd.DataFrame(data['daily']) if 'daily' in data else pd.DataFrame()


def fetch_space_weather():
    # NOAA SWPC example - Geomagnetic Activity Index (Kp)
    url = "https://services.swpc.noaa.gov/json/planetary_k_index_1m.json"
    response = requests.get(url)
    return pd.DataFrame(response.json())


def get_seasonal_events(year):
    ts = load.timescale()
    eph = load("de421.bsp")
    earth = eph["earth"]
    sun = eph["sun"]

    t0 = ts.utc(year, 1, 1)
    t1 = ts.utc(year, 12, 31)
    f = almanac.seasons(ts, eph)
    times, events = almanac.find_discrete(t0, t1, f)

    season_names = ['Spring Equinox', 'Summer Solstice', 'Autumn Equinox', 'Winter Solstice']
    return [(times[i].utc_iso(), season_names[events[i]]) for i in range(len(times))]


# === Runner ===
if __name__ == "__main__":
    print("Fetching Earth-related data sources...\n")

    start_time = "2025-01-01"
    end_time = "2025-04-01"

    # Climate WORKS
    print("[Open-Meteo] Sample Climate Data:")
    sample_climate = fetch_climate_data(latitude=40.7128, longitude=-74.0060, start_date=start_time, end_date=end_time)
    print(sample_climate.head())

    # Space Weather FAILS
    # space_weather = fetch_space_weather()
    # print("[SWPC] Sample Space Weather:", space_weather.head())

    # Geospatial FAILS
    # world = load_world_boundaries()
    # print("[Geo] Loaded boundaries for", len(world), "countries")

    # Seasonal FAILS
    # seasons = get_seasonal_events(2024)
    # print("[Skyfield] Seasonal Events in 2024:")
    # for date, event in seasons:
    #     print(" -", event, "on", date)

    print("\n✅ Earth data fetch complete.")
