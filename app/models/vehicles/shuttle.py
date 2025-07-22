from app.configs import VehicleConfig
from app.models.vehicles import Vehicle


class Shuttle(Vehicle):
    def __init__(self, config: VehicleConfig):
        super().__init__(config)

    def update(self):
        print("Shuttle update")

