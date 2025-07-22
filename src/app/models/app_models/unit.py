from pydantic import BaseModel

from src.utils.enums import UnitType
from src.utils.enums.unit_enums.prefix_enums import PrefixType


class Unit(BaseModel):
    type: UnitType = UnitType.NONE
    prefix: PrefixType = PrefixType.NONE
    amount: float

    @property
    def value(self) -> float:
        return self.amount * self.prefix.factor

    def __str__(self):
        return f"{self.amount} {self.prefix.symbol}{self.type.symbol}"

