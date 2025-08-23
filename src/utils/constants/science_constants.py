import json
from pathlib import Path

EARTH_GRAVITY = 9.81  # m/s²
ELECTRON_CHARGE = 1.602e-19  # C

def build_periodic_table() -> dict:
    filename = Path(__file__).resolve().parents[3] / "data" / "periodic-table.json"
    if not filename.is_file():
        raise FileNotFoundError(f"periodic-table.json not found at: {filename}")
    with filename.open("r", encoding="utf-8") as f:
        return json.load(f)

PERIODIC_TABLE = build_periodic_table()
