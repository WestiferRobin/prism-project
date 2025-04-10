import datetime
import random

def get_lunar_phase_data():
    phases = [
        "New Moon", "Waxing Crescent", "First Quarter", "Waxing Gibbous",
        "Full Moon", "Waning Gibbous", "Last Quarter", "Waning Crescent"
    ]
    return random.choice(phases)

def get_earth_data():
    now = datetime.datetime.now(datetime.UTC)
    return {
        "time": {
            "day_of_year": now.timetuple().tm_yday,
            "month": now.month,
            "week_of_year": now.isocalendar().week,
            "weekday": now.strftime('%A'),
            "lunar_phase": get_lunar_phase_data(),
        },
        "solar": {
            "solar_flux": random.uniform(60, 200),
            "sunspot_count": random.randint(0, 100),
            "geomagnetic_index": random.uniform(0, 10)
        },
        "weather": {
            "pressure": random.uniform(980, 1040),
            "wind_speed": random.uniform(0, 30),
            "temp": random.uniform(-10, 35)
        }
    }

def get_planet_data(start_date, end_date):
    colors = {
        "Sun": (255, 255, 0),
        "Earth": (0, 102, 255),
        "Moon": (200, 200, 200)
    }

    bodies = {
        "Earth": {"radius": 1.0, "period": 1.0},       # AU and years
        "Moon": {"radius": 0.00257, "period": 0.0748}  # AU and ~27.3 days
    }

    angles = {name: 0 for name in bodies}

    return {
        "colors": colors,
        "bodies": bodies,
        "angles": angles,
        "earth_data": get_earth_data(),
        "refresh_earth_data": get_earth_data,
        "start_date": start_date,
        "end_date": end_date
    }
