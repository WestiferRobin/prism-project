from simulations.app_simulations.fotf_game import run_fotf
from simulations.app_simulations.hedron_hive import run_hedron_hive
from simulations.app_simulations.prism_scribe import run_prism_scribe
from simulations.bot_simulations.arch_legion import run_arch_legion
from simulations.bot_simulations.orb_drone import run_orb_drone
from simulations.bot_simulations.prism_drone import run_prism_drone
from simulations.tool_simulations.mood_wave import run_mood_wave
from simulations.tool_simulations.nexus_theory import run_nexus_theory


def run_simulation(version: int, sub_version: int):
    if version == 0:  # Foundation and Survival
        run_mood_wave()
    elif version == 1:  # Recreate experiment and build on modular drone architecture
        if sub_version == 0:
            run_prism_drone()
        elif sub_version == 1:
            run_fotf()
    elif version == 2:  # Market and Share
        if sub_version == 0:
            run_hedron_hive()
        elif sub_version == 1:
            run_prism_scribe()
    elif version == 2:  # To Infinity and Beyond.
        if sub_version == 0:
            run_orb_drone()
        elif sub_version == 1:
            run_arch_legion()
    else:
        run_nexus_theory()
