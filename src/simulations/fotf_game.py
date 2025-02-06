
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