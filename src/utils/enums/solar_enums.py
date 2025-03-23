from enum import Enum

class SunColor(Enum):
    Yellow = 0
    Red = 1
    Blue = 2
    Orange = 3
    Black = 4

class SolarType(Enum):
    Sun = -3
    Asteroid = -2
    Moon = -1
    Terrestrial = 0
    Jovian = 1
    Dwarf = 2
