from src.models.equations.chemistry.density import Density
from src.models.equations.math.volume import Volume
from src.utils.enums.prefix_enums import PrefixType
from src.utils.enums.unit_enums import UnitType
from src.utils.unit import Unit


class Mass(Unit):
    volume: Volume
    density: Density

    def __init__(self, **mass_data):
        super().__init__(type=UnitType.GRAM, **mass_data)


    @property
    def amount(self) -> float:
        return self.volume.amount * self.density.amount


    @property
    def prefix(self) -> PrefixType:
        return self.density.prefix


    def __str__(self):
        return f"{self.amount} kg"

