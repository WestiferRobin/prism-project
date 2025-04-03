from src.models.fotf_models.solars.model import Solar
from src.utils.enums.solar_enums import SunColor, SolarType


class Sun(Solar):
    def __init__(self, sun_id, name: str, sun_color: SunColor = SunColor.Yellow):
        super().__init__(sun_id, name, SolarType.Sun)
        self.color = sun_color
