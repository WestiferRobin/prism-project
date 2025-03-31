from src.simulations.app_simulation import run_hedron_hive
from src.simulations.drone_simulation import run_prism_drone, run_orb_drone, run_arch_legion
from src.simulations.fotf_simulation import run_fotf
from src.simulations.tool_simulation import run_gold_goose, run_mood_wave


def run_simulation(version: int, sub_version: int):
    if version == 0:
        if sub_version == 0:
            run_fotf()
        elif sub_version == 1:
            run_gold_goose()
        elif sub_version == 2:
            run_mood_wave()
    elif version == 1:
        if sub_version == 0:
            run_prism_drone()
        elif sub_version == 1:
            run_hedron_hive()
        elif sub_version == 2:
            run_mood_wave()
    elif version == 2:
        if sub_version == 0:
            run_orb_drone()
        elif sub_version == 1:
            run_arch_legion()