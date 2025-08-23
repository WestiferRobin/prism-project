from typing import List, Dict

from pydantic import BaseModel

from src.models.equations.chemistry.mass import Mass
from src.models.equations.physics.force import Force
from src.utils.configs.model_configs.vehicle_configs import VehicleConfig
from src.utils.enums.vehicle_enums import VehicleType


class Vehicle(BaseModel):
    config: VehicleConfig

    def __init__(self, config: VehicleConfig, **vehicle_data):
        super().__init__(config=config, **vehicle_data)

    def __str__(self):
        return f"{self.config}"

    @property
    def type(self) -> VehicleType:
        return self.config.type

    @property
    def position(self) -> Dict[str, float]:
        return self.config.position

    @property
    def mass(self) -> Mass:
        return self.config.mass

    @property
    def forces(self) -> List[Force]:
        return self.config.forces

    @property
    def net_force(self) -> Force:
        net_force = Force()
        for force in self.forces:
            net_force += force
        return net_force

    # @property
    # def net_momentum(self) -> Momentum:
    #     pass

    def update(self):
        print("Vehicle update")

