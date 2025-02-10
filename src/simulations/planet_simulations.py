from src.models.planets.model import Planet, Sol
from src.models.vehicles.ships.star_ships import StarShip
from src.simulations.legion_simulation import simulate_star_cruiser, simulate_star_frigate, simulate_star_capital, \
    simulate_star_dreadnought


def simulate_planet_mission(home_planet: Planet, target_planet: Planet, ship: StarShip):
    pass

def simulate_lunar_mission(planet: Planet, ship: StarShip):
    for moon in planet.moons:
        pass

def simulate_star_base_missions(sol: Sol, ship: StarShip):
    simulate_lunar_mission(sol.earth, ship)
    simulate_planet_mission(sol.earth, sol.mars, ship)
    simulate_lunar_mission(sol.mars, ship)

def simulate_sol_missions():
    sol = Sol()
    fleet_ships = [
        simulate_star_cruiser(),
        simulate_star_frigate(),
        simulate_star_capital(),
        simulate_star_dreadnought()
    ]
    for fleet_ship in fleet_ships:
        simulate_star_base_missions(sol, fleet_ship)


if __name__ == "__main__":
    simulate_sol_missions()
