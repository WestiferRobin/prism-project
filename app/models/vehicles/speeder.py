from app.configs import VehicleConfig
from app.models.vehicles import Vehicle


class Speeder(Vehicle):
    def __init__(self, config: VehicleConfig):
        super().__init__(config)

    def update(self):
        print("Speeder update")

