from src.utils.enums.solar_enums import SolarType


class Solar:
    def __init__(self,
                 solar_id,
                 name: str,
                 solar_type: SolarType
                 ):
        self.id = solar_id
        self.name = name
        self.type = solar_type



