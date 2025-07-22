from enum import Enum


class UnitType(str, Enum):
    NONE = "none" # numbers? just data
    NEWTON = "newton" # force
    METER = "meter" # length
    GRAM = "gram" # mass
    SECOND = "second" # time
    AMPERE = "ampere" # current
    KELVIN = "kelvin" # temperature
    MOLE = "mole" # substance of mass
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

