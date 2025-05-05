from simulations.chemistry_simulations.atom_simulation import run_atom_simulation
from simulations.chemistry_simulations.molecule_simulation import run_molecule_simulation
from simulations.chemistry_simulations.reaction_simulation import run_reaction_simulation
from simulations.physics_simulations.classical_mechanics import run_classical_mechanics
from simulations.physics_simulations.electromagnetic_mechanics import run_electromagnetic_mechanics
from simulations.physics_simulations.newtonian_mechanics import run_newtonian_mechanics
from simulations.physics_simulations.nexus_mechanics import run_nexus_mechanics
from simulations.physics_simulations.quantum_mechanics import run_quantum_mechanics
from simulations.physics_simulations.relativistic_mechanics import run_relativistic_mechanics
from simulations.physics_simulations.statistical_mechanics import run_statistical_mechanics
from simulations.physics_simulations.thermo_dynamics import run_thermo_dynamics
from simulations.physics_simulations.wave_mechanics import run_wave_mechanics
from src.utils.exceptions.simulation_exceptions import VersionException

def run_chemistry_simulation(version: int):
    if version == 0:
        run_atom_simulation()
    elif version == 1:
        run_molecule_simulation()
    elif version == 2:
        run_reaction_simulation()
    else:
        raise VersionException(0, version)

def run_physics_simulation(version: int):
    """
    Simulates different levels of physics mechanics based on the selected version.

    Version Guide:
    0: Newtonian Mechanics
    1: Classical Mechanics
    2: Electromagnetic Mechanics
    3: Wave Mechanics
    4: Thermodynamics
    5: Statistical Mechanics
    6: Quantum Mechanics
    7: Relativistic Mechanics
    8: Nexus Mechanics (Unified Mechanics)

    GOAL:
    Model: q * (E(x, y) + v(t) × B(x, y)) = m(t) * g - m(t) * a(t)
    Interprets gravity as an emergent or equivalent electromagnetic force field.
    """
    if version == 0:
        run_newtonian_mechanics()
    elif version == 1:
        run_classical_mechanics()
    elif version == 2:
        run_electromagnetic_mechanics()
    elif version == 3:
        run_wave_mechanics()
    elif version == 4:
        run_thermo_dynamics()
    elif version == 5:
        run_statistical_mechanics()
    elif version == 6:
        run_quantum_mechanics()
    elif version == 7:
        run_relativistic_mechanics()
    elif version == 8:
        run_nexus_mechanics()
    else:
        raise VersionException(1, version)


def run_biology_simulation(version: int):
    """
    0: cell -> Prokaryotic and Eukaryotic
    1: bacteria and viruses
    2: plants and mushrooms
    3: animals
    """
    raise VersionException(2, version)

def run_full_simulation(version: int):
    raise VersionException(3, version)


def run_simulation(version: int, sub_version: int):
    if version == 0:  # Physics
        run_physics_simulation(version=sub_version)
    elif version == 1:  # Chemistry
        run_chemistry_simulation(version=sub_version)
    elif version == 2:  # Biology
        run_biology_simulation(version=sub_version)
    elif version == 3:  # All with AI
        run_full_simulation(version=sub_version)
    else:
        raise VersionException(version, sub_version)
