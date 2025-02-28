from src.models.drones.prism import PrismDrone
from src.models.legions.legion import LegionFleet, AdminFleet
from src.models.ships.space_ships import OrbDrone, SpaceSpeeder, SpaceInterceptor, SpaceShuttle, SpaceFighter, \
    SpaceBomber
from src.simulations.engine_simulations import run_engine_simulation
from src.simulations.armada_simulations import simulate_sol_missions
from src.simulations.prism_simulations import run_drone_simulations
from src.utils.enums.prism_enums import LegionRank


def run_orb_simulations(orb: OrbDrone):
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

def run_star_ship_simulations():
    simulate_sol_missions(star_ship=LegionFleet.build_cruiser_ship(3))
    simulate_sol_missions(star_ship=LegionFleet.build_cruiser_ship(2))
    simulate_sol_missions(star_ship=LegionFleet.build_cruiser_ship(1))
    simulate_sol_missions(star_ship=LegionFleet.build_cruiser_ship(0))

    simulate_sol_missions(star_ship=LegionFleet.build_frigate_ship(0))
    simulate_sol_missions(star_ship=LegionFleet.build_frigate_ship(1))
    simulate_sol_missions(star_ship=LegionFleet.build_frigate_ship(2))

    simulate_sol_missions(star_ship=LegionFleet.build_capital_ship(2))
    simulate_sol_missions(star_ship=LegionFleet.build_capital_ship(1))
    simulate_sol_missions(star_ship=LegionFleet.build_capital_ship(0))

    simulate_sol_missions(star_ship=AdminFleet.build_dreadnought_ship())


def run_ship_simulations():
    run_star_ship_simulations()
