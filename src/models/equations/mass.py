from src.models.equations.math.volume import Volume
from src.utils.unit import Unit


class Mass(Unit):
    volume: Volume
    density: Density

    def __init__(self, **mass_data):
        super().__init__(**mass_data)

