from src.models.drones.model import PrismDrone
from src.models.vehicles.ships.space_ships import OrbDrone, SpaceSpeeder, SpaceInterceptor, SpaceShuttle, SpaceFighter, \
    SpaceBomber
from src.simulations.engine_simulations import run_engine_simulation
from src.simulations.planet_simulations import simulate_sol_missions
from src.simulations.prism_simulations import run_drone_simulations


def run_orb_simulations(orb: OrbDrone):
    run_drone_simulations(orb.pilot)
    for engine in orb.engines:
        run_engine_simulation(engine)

def run_space_speeder_simulation(speeder: SpaceSpeeder):
    run_orb_simulations(speeder)

def run_space_ship_simulations():
    run_space_speeder_simulation(SpaceSpeeder(PrismDrone()))
    run_space_speeder_simulation(SpaceFighter(PrismDrone()))
    run_space_speeder_simulation(SpaceInterceptor(PrismDrone()))
    run_space_speeder_simulation(SpaceBomber(PrismDrone(), PrismDrone()))
    run_space_speeder_simulation(SpaceShuttle(PrismDrone(), PrismDrone(), (PrismDrone(), PrismDrone())))
    run_space_speeder_simulation(SpaceShuttle(PrismDrone(), PrismDrone(), (PrismDrone(), PrismDrone(), PrismDrone(), PrismDrone())))

def run_star_ship_simulations():
    simulate_sol_missions()


def run_ship_simulations():
    run_space_ship_simulations()
    run_star_ship_simulations()
