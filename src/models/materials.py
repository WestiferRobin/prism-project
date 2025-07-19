from pydantic import BaseModel, validator
from typing import Optional


class Metal(BaseModel):
    name: str
    density: float  # in g/cm³ (input), auto-converted to kg/m³ internally
    conductivity: Optional[float] = None  # in S/m
    magnetic: Optional[str] = None  # 'ferromagnetic', 'paramagnetic', 'diamagnetic'


# --- Define metals (densities in g/cm³) ---
METALS = {
    "gold": Metal(name="Gold", density=19.32, conductivity=4.1e7, magnetic='diamagnetic'),
    "silver": Metal(name="Silver", density=10.49, conductivity=6.3e7, magnetic='diamagnetic'),
    "copper": Metal(name="Copper", density=8.96, conductivity=5.96e7, magnetic='diamagnetic'),
    "aluminum": Metal(name="Aluminum", density=2.70, conductivity=3.5e7, magnetic='paramagnetic'),
    "titanium": Metal(name="Titanium", density=4.54, conductivity=2.4e6, magnetic='paramagnetic'),
    "iron": Metal(name="Iron", density=7.87, conductivity=1.0e7, magnetic='ferromagnetic'),
    "bismuth": Metal(name="Bismuth", density=9.78, conductivity=7.0e5, magnetic='diamagnetic'),
    "lead": Metal(name="Lead", density=11.34, conductivity=4.8e6, magnetic='diamagnetic'),
    "osmium": Metal(name="Osmium", density=22.59, conductivity=1.0e7, magnetic='paramagnetic'),
    "nickel": Metal(name="Nickel", density=8.90, conductivity=1.4e7, magnetic='ferromagnetic'),
}

