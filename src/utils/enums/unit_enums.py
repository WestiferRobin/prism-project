from enum import Enum


class UnitType(str, Enum):
    NONE = "none" # numbers? just dependencies
    NEWTON = "newton" # force of mass in acceleration or rate of mass in velocity
    JOULE = "joule" # basic macro energy of mass in work of force over distance
    METER = "meter" # length in distance
    GRAM = "gram" # mass as volume and density
    SECOND = "second" # time in space of volumes over time
    AMPERE = "ampere" # current in
    KELVIN = "kelvin" # temperature
    MOLE = "mole" # substance of mass
    DENSITY = "density" # density of mass
    CANDELA = "candela" # light

    @property
    def symbol(self) -> str:
        return {
            UnitType.NEWTON: "N",
            UnitType.METER: "m",
            UnitType.GRAM: "g",
            UnitType.SECOND: "s",
            UnitType.AMPERE: "A",
            UnitType.KELVIN: "K",
            UnitType.MOLE: "mol",
            UnitType.CANDELA: "cd",
            UnitType.NONE: ""
        }[self]

