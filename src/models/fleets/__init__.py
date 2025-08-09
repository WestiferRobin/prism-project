from pydantic import BaseModel

from src.utils.configs import Config


class ShipConfig(Config):
    pass


class FleetConfig(Config):
    lead_ship_config: ShipConfig



class Fleet(BaseModel):
    config: FleetConfig

