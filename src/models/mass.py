from src.enums.unit_enums import UnitType
from src.enums.unit_enums.prefix_enums import PrefixType
from src.models.unit import Unit


class Mass(Unit):
    def __init__(self,
        amount: float,
        prefix: PrefixType
    ):
        super().__init__(
            amount=amount,
            prefix=prefix,
            type=UnitType.GRAM
        )

