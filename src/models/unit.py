from pydantic import BaseModel

from src.enums.unit_enums import UnitType
from src.enums.unit_enums.prefix_enums import PrefixType


class Unit(BaseModel):
    type: UnitType = UnitType.NONE
    prefix: PrefixType = PrefixType.NONE
    amount: float

    @property
    def value(self) -> float:
        return self.amount * self.prefix.factor

    def __str__(self):
        return f"{self.amount} {self.prefix.symbol}{self.type.symbol}"


class Mass(Unit):
    def __init__(self,
        amount: float,
        prefix: PrefixType = PrefixType.KILO
    ):
        super().__init__(
            amount=amount,
            prefix=prefix,
            type=UnitType.GRAM
        )

