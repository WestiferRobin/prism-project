from src.models.drones.prism_drone import PrismAgent, PrismDrone
from src.models.vehicles.ships.space_ships import SpaceShip

class OrbDrone(SpaceShip):
    def __init__(self, pilot_id, co_pilot: PrismAgent):
        super().__init__(pilot_id, PrismDrone(co_pilot))

if __name__ == "__main__":
    drone = PrismDrone()
    print(drone.mass())
