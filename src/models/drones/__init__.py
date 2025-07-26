from pydantic import BaseModel

from src.models.prisms import Prism
from src.utils.configs.drone_config import DroneConfig


class Drone(BaseModel):
    config: DroneConfig

    def __init__(self, config: DroneConfig, **drone_data):
        super().__init__(config=config, **drone_data)


    @property
    def prism(self) -> Prism:
        prism_config = self.config.prism
        return Prism(config=prism_config)