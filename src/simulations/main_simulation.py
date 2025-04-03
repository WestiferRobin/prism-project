from src.simulations.app_simulations.fotf_game import run_fotf
from src.simulations.app_simulations.hedron_hive import run_hedron_hive
from src.simulations.app_simulations.prism_scribe import run_prism_scribe
from src.simulations.bot_simulations.arch_legion import run_arch_legion
from src.simulations.bot_simulations.orb_drone import run_orb_drone
from src.simulations.bot_simulations.prism_drone import run_prism_drone
from src.simulations.tool_simulations.golden_goose import run_golden_goose
from src.simulations.tool_simulations.mood_wave import run_mood_wave
from src.simulations.tool_simulations.nexus_theory import run_nexus_theory


def run_simulation(version: int, sub_version: int):
    if version == 0: # Foundation and Survival
        if sub_version == 0:
            run_golden_goose()
        elif sub_version == 1:
            run_mood_wave()
        elif sub_version == 2:
            run_prism_drone()
    elif version == 1: # Market and Share
        if sub_version == 0:
            run_fotf()
        elif sub_version == 1:
            run_prism_scribe()
        elif sub_version == 2:
            run_hedron_hive()
    elif version == 2: # To Infinity and Beyond.
        if sub_version == 0:
            run_orb_drone()
        elif sub_version == 1:
            run_arch_legion()
    else:
        run_nexus_theory()