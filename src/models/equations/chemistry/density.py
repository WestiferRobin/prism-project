from src.utils.enums.prefix_enums import PrefixType
from src.utils.enums.unit_enums import UnitType
from src.utils.unit import Unit


class Density(Unit):
    def __init__(self,
        prefix: PrefixType = PrefixType.CENTI,
        **unit_data
    ):
        super().__init__(
            type=UnitType.DENSITY,
            prefix=prefix,
            **unit_data
        )

