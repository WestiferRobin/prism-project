from src.models.drones.model import PrismAgent

def nexus_simulation(engine: NexusEngine):
    run_engine_simulation(engine)
    run_orb_simulation(engine)
    run_prism_simulation(engine)

def engine_simulation(nexus_engine: NexusEngine):
    nexus_engine = NexusEngine()
    nexus_simulation(engine=NexusEngine())


def orb_simulation():
    pilot = PrismAgent()
    craft = OrbDrone(pilot)
    for engine in craft:
        engine_simulation(engine)
    # get craft = OrbDrone(PrismAgent())
    # craft going to orbit at c
    # craft going to earth to luna at c
    # craft going from earth to:
    #   - mars, venus, gas giant, giant moons
    #   - Sol to Sov Solar Systems in Atlas Galaxy

def space_ship_simulations():
    # study data from orb simulations
    # Note: Needs number of engines for configuration
    ships = (
        OrbDrone(1)
        SpaceCycle(2),
        SpaceTank(3),
        SpaceSpeeder(4),
        SpaceFighter(6),
        SpaceShuttle(9),
        SpaceGunship(12),
        SpaceTransport(16)
    )
    for ship in ships:
        ship_simulation(ship)
    return ships

def solar_ship_simulations():
    # study data from Sol and ships
    ships = (
        SolarProbe()
        SolarCruiser(),
        SolarFrigate(),
        SolarShip(),
        SolarDreadnought()
    )
    for ship in ships:
        ship_simulation(ship)
    return ships


def legion_armada_simulations():
    armada = {
        "solar_ships": solar_ship_simulations(),
        "space_ships": space_ship_simulations(),
    }
    """

    Land is ArmadaBase on Planet
    Space is StationBase in Orbit
    Solar:
    - Probe(64 as 1 SolarEngine) is OrbDrone(1 Nexus Engine)
    - Cruiser(2)
    - Frigate(4)
    - Solarship(8)
    - Dreadnought(16)
    - Station(64 SolarEngines)

    SolarProbe is OrbDrone
    SpaceCycle is OrbDrone
    SpaceTank is SpaceSpeeder

    """

def sov_fleet_simulations():
    legion_armada = legion_armada_simulations()
    ship = LegionCruiser()
    base = LegionBase()
    # ship invades base with defense fleet
    # ship invades base with no fleet
    # ship visits base in invasion battle
    # ship visits base in trade route
    # TODO: Needs Soul Saga and Prequels finished


class LegionArmada:
    def __init__(self):
        self.active_fleets = []
        self.base_fleet = []

class PrismAvatar(PrismAgent):

class AdminLegion:
    def __init__(self, username: str, user_tag: str, user_id):
        self.leader = PrismAvatar(name=username, seed=user_id, )
        self.armada = LegionArmada()
        self.bases = {}


if __name__ == "__main__":
    # TODO: STOP EVERYTHING AND START nexus_mechanics.py
    # run_engine_simulation()

    # This is the idea how my LegionArmada would look like
