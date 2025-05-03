from simulations.biology_simulation import run_biology_simulation
from simulations.chemistry_simulation import run_chemistry_simulation
from simulations.physics_simulation import run_physics_simulation
from utils.exceptions import VersionException


def run_full_simulation(version: int):
    raise VersionException(3, version)


def run_simulation(version: int = 0, sub_version: int = 0):
    if version == 0:  # Chemistry
        run_chemistry_simulation(version=sub_version)
    elif version == 1:  # Physics
        run_physics_simulation(version=sub_version)
    elif version == 2:  # Biology
        run_biology_simulation(version=sub_version)
    elif version == 3:  # All with AI
        run_full_simulation(version=sub_version)
    else:
        raise VersionException(version, sub_version)
