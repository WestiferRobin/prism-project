from src.models.drones.prism import PrismDrone
from src.models.ships.space_ships import SpaceSpeeder
from src.models.weapons.range_weapons import PlasmaCannon
from src.models.weapons.range_weapons.vehicle_weapons.turret_weapon import LaserTurret


class SpaceShuttle(SpaceSpeeder):
    def __init__(self, pilot: PrismDrone, co_pilot: PrismDrone, crew=None):
        super().__init__(pilot=pilot, right_cannon=PlasmaCannon(), left_cannon=PlasmaCannon())
        self.co_pilot = co_pilot
        self.armor = 75
        self.shields = 50

        if crew is None:
            crew = tuple([self.pilot, self.co_pilot])
        else:
            shuttle_crew = [self.pilot, self.co_pilot]
            for member in crew:
                shuttle_crew.append(member)
            crew = tuple(shuttle_crew)
        self.crew = crew

class SpaceGunship(SpaceShuttle):
    def __init__(self, pilot: PrismDrone, co_pilot: PrismDrone, crew=None):
        super().__init__(pilot=pilot, co_pilot=co_pilot, crew=crew)
        self.armor += 25

        self.front_turret = LaserTurret()
        self.back_turret = LaserTurret()

class SpaceCarrier(SpaceShuttle):
    def __init__(self, pilot: PrismDrone, co_pilot: PrismDrone, crew=None, cargo=None):
        super().__init__(pilot=pilot, co_pilot=co_pilot, crew=crew)

        self.cargo = cargo