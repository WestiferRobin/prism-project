from uuid import UUID

from src.models.drones.model import PrismDrone
from src.models.games.fotf_game import FotfGame
from src.models.vehicles.ships.space_ships import OrbProbe
from src.simulations.game_simulations import run_game_simulations
from src.simulations.prism_simulations import run_drone_simulations
from src.simulations.ship_simulations import run_orb_simulations, run_ship_simulations
from src.utils.enums.prism_enums import LegionRank


def run_test_simulation(pilot: PrismDrone, is_final: bool=False):
    if is_final:
        run_drone_simulations(pilot)
        run_orb_simulations(orb=OrbProbe(pilot))
        run_ship_simulations(pilot)
        run_game_simulations(pilot)
    else:
        print("Debugging")
        # run_drone_simulations(pilot)
        # run_orb_simulations(orb=OrbProbe(pilot))
        # run_ship_simulations(pilot)
        run_game_simulations(pilot)

def run_final_simulation(drone: PrismDrone):
    run_test_simulation(drone, is_final=True)
    game = FotfGame(drone)
    game.start()
    # TODO: Build the model to show in pygame like unity or unreal?

def run_simulation(is_debug: bool):
    prism_drone = PrismDrone(
        prism_id=UUID('00000000-0000-0000-0000-000000000000'),
        name="Wes",
        rank=LegionRank.Arch,
        age=31,
        gender=True
    )
    if is_debug:
        run_test_simulation(prism_drone)
    else:
        run_final_simulation(prism_drone)

if __name__ == "__main__":
    run_simulation(is_debug=True)

