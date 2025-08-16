from src.utils.enums.prefix_enums import PrefixType
from src.utils.enums.unit_enums import UnitType
from src.utils.unit import Unit


class Volume(Unit):
    def __init__(self,
        volume_type: UnitType = UnitType.GRAM,
        prefix_type: PrefixType = PrefixType.CENTI,
        **unit_data
    ):
        super().__init__(
            type=volume_type,
            prefix=prefix_type,
            **unit_data
        )

