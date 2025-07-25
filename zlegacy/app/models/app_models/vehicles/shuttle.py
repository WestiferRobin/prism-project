from src.utils.configs import VehicleConfig
from zlegacy.app.models.app_models.vehicles import Vehicle


class Shuttle(Vehicle):
    def __init__(self, config: VehicleConfig):
        super().__init__(config)

    def update(self):
        print("Shuttle update")

