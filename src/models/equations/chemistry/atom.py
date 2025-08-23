from typing import List, Dict

from pydantic import BaseModel

from src.models.equations.math import Position


class Atom(BaseModel):
    number: int
    symbol: str

    period: int
    group: int
    name: str
    description: str # appearance
    atomic_mass: float

    density: float
    boil_point: float
    melt_point: float
    molar_heat: float

    position: Position
    shells: List[int]
    electron_configuration: str
    charge: float = 0

    @property
    def protons(self) -> int:
        return self.number

    @property
    def electrons(self) -> int:
        return self.number - int(self.charge)

    @property
    def neutrons(self) -> int:
        neutrons = self.mass_number - self.number
        return max(neutrons, 0)

    @property
    def quarks(self) -> Dict[str, int]:
        quark = self.mass_number if self.mass_number is not None else int(round(self.atomic_mass))
        return {
            "up": quark + self.number,
            "down": 2 * quark - self.number,
        }

    @property
    def baryon_number(self):
        return self.mass_number

    @property
    def leptons_number(self):
        return self.mass_number

    def __str__(self):
        return f"{self.symbol}"

