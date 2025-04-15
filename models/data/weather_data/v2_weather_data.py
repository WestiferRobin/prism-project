from io import StringIO

import requests
import pandas as pd
import datetime


def fetch_usgs_earthquakes(start_date, end_date, min_magnitude=4.5):
    # Split date range into 90-day chunks to avoid 20,000 result cap
    start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    all_data = []

    while start < end:
        chunk_end = min(start + datetime.timedelta(days=90), end)
        url = (
            f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={start.date()}"
            f"&endtime={chunk_end.date()}&minmagnitude={min_magnitude}"
        )
        response = requests.get(url)
        try:
            data = response.json()
            if 'features' in data:
                all_data.extend(data['features'])
        except Exception as e:
            print(f"[USGS] Failed to parse data from {start.date()} to {chunk_end.date()}:", e)
        start = chunk_end + datetime.timedelta(days=1)

    return pd.json_normalize(all_data) if all_data else pd.DataFrame()


def fetch_ibtracs_hurricanes(start_date, end_date):
    # NOAA IBTrACS filtering endpoint (indirect via CSV filter logic)
    url = "https://www.ncei.noaa.gov/data/international-best-track-archive-for-climate-stewardship-ibtracs/v04r00/access/csv/ibtracs.ALL.list.v04r00.csv"
    response = requests.get(url)
    if response.status_code != 200:
        print("[IBTrACS] Failed to download hurricane data.")
        return pd.DataFrame()

    df = pd.read_csv(StringIO(response.text))
    df["ISO_TIME"] = pd.to_datetime(df["ISO_TIME"], errors="coerce")
    df = df[(df["ISO_TIME"] >= pd.to_datetime(start_date)) & (df["ISO_TIME"] <= pd.to_datetime(end_date))]
    return df[["SID", "SEASON", "BASIN", "NAME", "ISO_TIME", "LAT", "LON", "USA_WIND"]].dropna()


def fetch_global_fires(start_date, end_date, product="VIIRS", region="Global"):
    """
    Fetches active fire data from NASA FIRMS archive.
    Product: MODIS or VIIRS
    Region: Global, Africa, Asia, Europe, etc.
    """
    # Normalize product + region
    product = product.upper()
    region = region.capitalize()

    base_url = "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/6"
    product_path = f"{product}/"
    day_range = pd.date_range(start=start_date, end=end_date)

    all_dfs = []

    for day in day_range:
        date_str = day.strftime("%Y/%j")  # YYYY/DDD (Julian day)
        file_url = (
            f"{base_url}/{product_path}{date_str}/"
            f"{product}_C6_{region}_7d.csv"
        )

        try:
            print(f"[FIRMS] Fetching: {file_url}")
            response = requests.get(file_url)
            if response.status_code == 200:
                df = pd.read_csv(StringIO(response.text))
                df["acq_date"] = pd.to_datetime(df["acq_date"], errors="coerce")
                all_dfs.append(df)
            else:
                print(f"[FIRMS] No data for {day.date()} ({response.status_code})")
        except Exception as e:
            print(f"[FIRMS] Error for {day.date()}: {e}")

    return pd.co


# === Runner ===
if __name__ == "__main__":
    print("Fetching Earth-related weather v2 data sources...\n")

    start_time = "2023-01-01"
    end_time = "2024-01-01"

    # Disasters WORKS
    quakes = fetch_usgs_earthquakes(start_time, end_time)
    print("[USGS] Sample Earthquakes:", quakes[['properties.place', 'properties.mag']].head(), len(quakes))

    # Hurricanes WORKS (TODO: only for training... needs live data later)
    hurricanes = fetch_ibtracs_hurricanes(start_time, end_time)
    print("[IBTrACS] Sample Hurricanes:", hurricanes.head())

    # FAILS
    fires = fetch_global_fires(start_time, end_time)
    print("[FIRMS] Sample Fires:", fires.head())

    print("\n✅ v2 Weather data fetch complete.")
