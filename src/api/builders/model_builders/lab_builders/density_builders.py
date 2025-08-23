from src.models.equations.chemistry.density import Density
from src.utils.enums.prefix_enums import PrefixType


def build_density(amount: float, prefix: PrefixType) -> Density:
    return Density(amount=amount, prefix=prefix)


def build_water_density(amount: float, prefix: PrefixType = PrefixType.CENTI) -> Density:
    return build_density(amount=amount, prefix=prefix)

