from src.utils.enums.planet_enums import SunType


class Sun:
    def __init__(self, name: str, sun_type: SunType = SunType.Yellow):
        self.name = name
        self.type = sun_type