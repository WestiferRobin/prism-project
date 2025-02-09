from src.models.drones.model import PrismDrone
from src.models.vehicles.ships.space_ships import SpaceFighter, SpaceShuttle
from src.models.vehicles.ships.star_ships import StarCruiser, StarFrigate, StarCapital, StarDreadnought
from src.utils.enums.prism_enums import DroneRank


def build_drone_squadron(leader: PrismDrone = None):
    if leader is None:
        leader = PrismDrone(rank=DroneRank.Sergeant)
    squadron = (
        leader,
        PrismDrone(rank=DroneRank.Lance),
        PrismDrone(rank=DroneRank.Corporal),
        PrismDrone(rank=DroneRank.Corporal),
        PrismDrone(rank=DroneRank.Private),
        PrismDrone(rank=DroneRank.Private),
        PrismDrone(rank=DroneRank.Private),
        PrismDrone(rank=DroneRank.Private)
    )
    return squadron

def build_fighter_squadron():
    leader = SpaceFighter(PrismDrone(rank=DroneRank.Lance))
    squadron = (
        leader,
        SpaceFighter(PrismDrone(rank=DroneRank.Lance)),
        SpaceFighter(PrismDrone(rank=DroneRank.Lance)),
        SpaceFighter(PrismDrone(rank=DroneRank.Corporal)),
        SpaceFighter(PrismDrone(rank=DroneRank.Corporal)),
        SpaceFighter(PrismDrone(rank=DroneRank.Corporal))
    )
    return squadron

def build_shuttle_squadron():
    squadron = build_drone_squadron()
    lead_pilot = squadron[1]
    co_pilot = squadron[2]
    crew = (
        squadron[0],
        squadron[3:]
    )
    return SpaceShuttle(lead_pilot, co_pilot, crew)

def build_star_cruiser():
    return StarCruiser()

def build_star_frigate():
    return StarFrigate()

def build_star_capital():
    return StarCapital()

def build_star_dreadnought():
    return StarDreadnought()

def build_star_fleet():
    star_cruiser = build_star_cruiser()
    star_frigate = build_star_frigate()
    star_capital = build_star_capital()
    fleet = (
        star_cruiser,
        star_frigate,
        star_capital,
    )
    return fleet

def build_star_armada():
    flagship = build_star_dreadnought()
    elite_fleet = (
        flagship,
        build_star_capital(),
        build_star_capital()
    )
    armada = (
        elite_fleet,
        build_star_fleet(),
        build_star_fleet()
    )
    return armada

if __name__ == "__main__":
    star_armada = build_star_armada()
    print(star_armada)



