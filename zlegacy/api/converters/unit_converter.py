from src.utils.enums.unit_enums.prefix_enums import PrefixType
from zlegacy.app.models.app_models.unit import Unit


def convert_unit(unit: Unit, prefix: PrefixType) -> Unit:
    unit_value = unit.value
    converted_amount = unit_value / prefix.factor

    return Unit(
        amount=converted_amount,
        prefix=prefix,
        type=unit.type,
    )
