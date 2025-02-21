from src.models.drones.model import PrismDrone
from src.models.vehicles.ships.space_ships import OrbProbe, SpaceSpeeder, SpaceInterceptor, SpaceShuttle, SpaceFighter, \
    SpaceBomber
from src.models.vehicles.ships.star_ships import StarFrigate, StarCruiser, StarCapital, StarDreadnought
from src.simulations.engine_simulations import run_engine_simulation
from src.simulations.planet_simulations import simulate_sol_missions
from src.simulations.prism_simulations import run_drone_simulations
from src.utils.enums.prism_enums import LegionRank


def run_orb_simulations(orb: OrbProbe):
    run_drone_simulations(orb.pilot)
    for engine in orb.engines:
        run_engine_simulation(engine)

def run_space_speeder_simulation(speeder: SpaceSpeeder):
    run_orb_simulations(speeder)

def run_space_ship_simulations(pilot: PrismDrone):
    run_space_speeder_simulation(SpaceSpeeder(pilot))
    run_space_speeder_simulation(SpaceFighter(pilot))
    run_space_speeder_simulation(SpaceInterceptor(pilot))
    run_space_speeder_simulation(SpaceBomber(pilot, PrismDrone(rank=LegionRank.Ensign)))
    run_space_speeder_simulation(SpaceShuttle(PrismDrone(), PrismDrone(), (pilot, PrismDrone())))
    run_space_speeder_simulation(SpaceShuttle(pilot, PrismDrone(), (PrismDrone(), PrismDrone(), PrismDrone(), PrismDrone())))

def run_star_ship_simulations(lead_officer: PrismDrone):
    simulate_sol_missions(star_ship=StarCruiser(lead_officer))
    simulate_sol_missions(star_ship=StarFrigate(lead_officer))
    simulate_sol_missions(star_ship=StarCapital(lead_officer))
    simulate_sol_missions(star_ship=StarDreadnought(lead_officer))


def run_ship_simulations(drone: PrismDrone):
    run_space_ship_simulations(pilot=drone)
    run_star_ship_simulations(lead_officer=drone)
