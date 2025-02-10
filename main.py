import uuid

from src.models.drones.model import PrismDrone
from src.models.legion import AdminLegion
from src.models.vehicles.ships.space_ships import OrbDrone
from src.simulations.game_simulations import run_game_simulations
from src.simulations.prism_simulations import run_drone_simulations
from src.simulations.ship_simulations import run_orb_simulations, run_ship_simulations

def run_unit_simulation():
    orb = OrbDrone(PrismDrone())
    run_drone_simulations(orb.pilot)
    run_orb_simulations(orb)

def run_debug_simulation():
    run_unit_simulation()
    # run_ship_simulations()

def run_test_simulation():
    run_unit_simulation()
    run_ship_simulations()

def run_final_simulation():
    run_test_simulation()
    run_game_simulations()

def run_simulation(is_debug: bool):
    if is_debug:
        run_debug_simulation()
    else:
        run_final_simulation()


if __name__ == "__main__":
    run_simulation(is_debug=True)
    # When merged and finished final simulation:
        # Update both computers to latest python
        # Create a rest api in prism-agent-service using nexus_framework
        # Create a frontend app in prism-web-app using react with prism-agent-service locally

