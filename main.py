from uuid import UUID

from src.models.drones.orb import OrbDrone
from src.models.drones.prism import PrismDrone
from src.models.games.fotf_game import FotfGame
from src.simulations.fotf_simulations import run_game_simulations
from src.simulations.prism_simulations import run_drone_simulations
from src.simulations.ship_simulations import run_orb_simulations, run_ship_simulations
from src.utils.enums.prism_enums import LegionRank

def run_simulation(player: PrismDrone):
    run_drone_simulations(player)
    run_

if __name__ == "__main__":
    avatar = PrismDrone(
        prism_id=UUID('00000000-0000-0000-0000-000000000000'),
        name="Wes",
        rank=LegionRank.Sergeant,
        age=32,
        gender=True
    )
    run_simulation(avatar)

