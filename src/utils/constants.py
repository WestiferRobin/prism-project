import os

LAB_VERSION = 0

GRAVITY = 9.8
SAMPLE_MOLECULES_NAMES = {
    "H2O": "Water",
    "CO2": "Carbon Dioxide",
    "O2": "Oxygen",
    "N2": "Nitrogen",
    "CH4": "Methane",
    "NH3": "Ammonia",
    "H2O2": "Hydrogen Peroxide",
    "C6H12O6": "Glucose",
    "C2H6": "Ethane",
    "C2H4": "Ethene",
    "C2H2": "Ethyne",
    "C6H6": "Benzene",
}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
PERIODIC_TABLE_PATH = os.path.join(BASE_DIR, 'data', 'periodic-table.json')

