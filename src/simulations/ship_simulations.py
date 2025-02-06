
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
