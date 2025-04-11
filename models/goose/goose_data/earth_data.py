import datetime
from skyfield.api import load, load_constellation_map
import pandas as pd

def calculate_solar_data(start_date: datetime.date, end_date: datetime.date):
    # Load ephemeris and timescale
    planets = load('de421.bsp')
    ts = load.timescale()
    constellation_at = load_constellation_map()

    # Celestial bodies
    earth = planets['earth']
    sun = planets['sun']
    moon = planets['moon']
    mars = planets['mars']

    # Generate list of dates
    dates = [
        start_date + datetime.timedelta(days=i)
        for i in range((end_date - start_date).days + 1)
    ]

    records = []

    for d in dates:
        t = ts.utc(d.year, d.month, d.day)
        record = {'date': d.isoformat()}

        # Positions (relative to Sun or Earth)
        earth_pos = planets['sun'].at(t).observe(earth).apparent().position.au
        moon_pos = earth.at(t).observe(moon).apparent().position.au
        mars_pos = planets['sun'].at(t).observe(mars).apparent().position.au

        # Add XYZ positions
        record.update({
            'earth_x': earth_pos[0], 'earth_y': earth_pos[1], 'earth_z': earth_pos[2],
            'moon_x': moon_pos[0], 'moon_y': moon_pos[1], 'moon_z': moon_pos[2],
            'mars_x': mars_pos[0], 'mars_y': mars_pos[1], 'mars_z': mars_pos[2],
        })

        # Get RA/DEC and constellation (zodiac sign)
        sun_ast = earth.at(t).observe(sun).apparent()
        moon_ast = earth.at(t).observe(moon).apparent()

        sun_const = constellation_at(sun_ast)
        moon_const = constellation_at(moon_ast)

        record['sun_zodiac'] = sun_const
        record['moon_zodiac'] = moon_const

        records.append(record)

    # Save to CSV
    df = pd.DataFrame(records)
    df.to_csv(f"solar_data_{start_date}_{end_date}.csv", index=False)
    print(f"Saved {len(records)} days to solar_data_{start_date}_{end_date}.csv")

if __name__ == "__main__":
    start_d = datetime.date(1925, 1, 1)
    end_d = datetime.date(2025, 4, 10)

    calculate_solar_data(start_d, end_d)
