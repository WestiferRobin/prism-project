import datetime
from skyfield.api import load
import pandas as pd

from models.ui.solar_system_ui import run_solar_system_ui


def load_solar_data(start_date: datetime.datetime, end_date: datetime.datetime, is_ui: bool = False):
    # Load ephemeris and timescale
    planets = load('data/solar_data/de440s.bsp')
    ts = load.timescale()

    # List of all major planets
    planet_names = [
        'mercury barycenter', 'venus barycenter', 'earth barycenter', 'mars barycenter',
        'jupiter barycenter', 'saturn barycenter',
        'uranus barycenter', 'neptune barycenter'
    ]

    # Generate list of dates
    dates = [
        start_date + datetime.timedelta(days=i)
        for i in range((end_date - start_date).days + 1)
    ]

    records = []

    for d in dates:
        t = ts.utc(d.year, d.month, d.day)
        record = {'date': f"{d.date()}"}

        sun_pos = planets['sun'].at(t).position.au

        for name in planet_names:
            short = name.split()[0]  # Use 'jupiter' from 'jupiter barycenter'
            pos = planets[name].at(t).position.au
            rel = [p - s for p, s in zip(pos, sun_pos)]
            record.update({
                f'{short}_x': rel[0],
                f'{short}_y': rel[1],
                f'{short}_z': rel[2],
            })

        # Add Earth's Moon separately
        earth_pos = planets['earth'].at(t).position.au
        moon_pos = planets['moon'].at(t).position.au
        moon_rel = [m - e for m, e in zip(moon_pos, earth_pos)]
        record.update({
            'moon_x': moon_rel[0],
            'moon_y': moon_rel[1],
            'moon_z': moon_rel[2],
        })

        records.append(record)

    # Save to CSV
    df = pd.DataFrame(records)
    df.to_csv(f"data/solar_data/solar_data_{start_date.date()}_{end_date.date()}.csv", index=False)

    if is_ui:
        run_solar_system_ui(start_date, end_date)

    return df
