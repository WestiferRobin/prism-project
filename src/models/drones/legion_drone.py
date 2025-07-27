from src.models.drones import Drone
from src.utils.configs.model_configs.drone_config import DroneConfig

TEMP_MAX = 100

class LegionDrone(Drone):
    health: int = TEMP_MAX
    armor: int = TEMP_MAX # TODO: When simulated, make this into a class
    shields: int = TEMP_MAX # TODO: Make shields come from

    def __init__(self, config: DroneConfig, **drone_data) -> None:
        super().__init__(config=config, **drone_data)


    def heal(self) -> None:
        self.health = TEMP_MAX

    def repair(self) -> None:
        self.armor = TEMP_MAX

    def recharge(self) -> None:
        self.shields = TEMP_MAX