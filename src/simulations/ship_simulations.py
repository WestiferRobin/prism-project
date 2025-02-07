from src.models.drones.model import PrismDrone
from src.models.vehicles.ships.space_ships import OrbDrone
from src.simulations.engine_simulations import run_engine_simulation
from src.simulations.prism_simulations import run_drone_simulations


def run_orb_simulations():
    drone = PrismDrone()
    run_drone_simulations(drone)
    orb = OrbDrone(drone.brain)
    for engine in orb.engines:
        run_engine_simulation(engine)


def run_space_ship_simulations():
    run_orb_simulations()
    # run_space_speeder()
    # run_space_fighter()
    # run_space_shuttle()


def run_star_ship_simulations():
    pass
    # run_star_cruiser_simulations
    # run_star_frigate_simulations
    # run_star_capital_simulations
    # run_star_dreadnought_simulations


def run_ship_simulations():
    run_space_ship_simulations()
    run_star_ship_simulations()
