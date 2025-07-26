from typing import List, Dict

from src.utils.configs import VehicleConfig
from src.utils.enums import VehicleType
from zlegacy.models import Model
from zlegacy.models import Force
from zlegacy.models.app_models.equations.chemistry.mass import Mass


class Vehicle(Model):
    config: VehicleConfig

    def __init__(self, config: VehicleConfig):
        super().__init__(name=config.name, config=config)

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

    @property
    def net_momentum(self) -> Momentum:

    def update(self):
        print("Vehicle update")

