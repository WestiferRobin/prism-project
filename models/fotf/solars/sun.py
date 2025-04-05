from models.fotf.solars.model import Solar
from utils.enums.solar_enums import SunColor, SolarType


class Sun(Solar):
    def __init__(self, sun_id, name: str, sun_color: SunColor = SunColor.Yellow):
        super().__init__(sun_id, name, SolarType.Sun)
        self.color = sun_color
