from src.models.drones.model import PrismDrone
from src.models.legion import LegionFleet
from src.models.planets.model import Planet, Sol
from src.models.vehicles.ships.star_ships import StarShip, StarCapital
from src.utils.enums.prism_enums import LegionRank


def simulate_planet_mission(target_planet: Planet, star_ship: StarShip):
    star_ship.current_planet = target_planet

def simulate_lunar_mission(planet: Planet, star_ship: StarShip):
    simulate_planet_mission(planet, star_ship)
    for moon in planet.moons:
        simulate_planet_mission(moon, star_ship)
        simulate_planet_mission(planet, star_ship)

def simulate_star_base_missions(sol: Sol, star_ship: StarShip):

    # LunaBase Mission 1
    simulate_planet_mission(sol.earth, star_ship)
    simulate_lunar_mission(sol.earth, star_ship)

    # StarBase Mission 1 and LunaBase Mission 2 & 3
    simulate_planet_mission(sol.mars, star_ship)
    simulate_lunar_mission(sol.mars, star_ship)

    # TerraStation Missions 1 and 2
    simulate_planet_mission(sol.venus, star_ship)
    simulate_planet_mission(sol.mercury, star_ship)

    # JovianStation Mission 1
    simulate_planet_mission(sol.jupiter, star_ship)
    simulate_lunar_mission(sol.jupiter, star_ship)

    # JovianStation Mission 1
    simulate_planet_mission(sol.saturn, star_ship)
    simulate_lunar_mission(sol.saturn, star_ship)

    # JovianStation Mission 2
    simulate_planet_mission(sol.uranus, star_ship)

    # JovianStation Mission 3
    simulate_planet_mission(sol.neptune, star_ship)
    simulate_lunar_mission(sol.neptune, star_ship)

    # DwarfStation Mission 1
    simulate_planet_mission(sol.pluto, star_ship)

    # TODO: figure out interstellar missions

def simulate_sol_missions(star_ship: StarShip):
    sol = Sol()
    simulate_star_base_missions(sol, star_ship)


if __name__ == "__main__":
    fleet_officer = PrismDrone(rank=LegionRank.Arch)
    legion_fleet = LegionFleet(StarCapital(fleet_officer))
    for ship in legion_fleet.ships:
        simulate_sol_missions(ship)
