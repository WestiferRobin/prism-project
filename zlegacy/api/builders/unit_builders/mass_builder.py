from src.utils.enums import PrefixType
from zlegacy.app.models.app_models.equations.chemistry.mass import Mass


def build_mass(amount: float, prefix: PrefixType) -> Mass:
    return Mass(amount=amount, prefix=prefix)


def build_gram_mass(amount: float) -> Mass:
    return Mass(amount=amount, prefix=Mass.GRAM)


def build_kilo_mass(amount: float) -> Mass:
    return Mass(amount=amount, prefix=PrefixType.KILO)

