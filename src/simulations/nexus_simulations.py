import uuid

from src.models.drones.model import PrismCell
from src.models.vehicles.model import NexusEngine
from src.simulations.engine_simulations import run_engine_simulation
from src.utils.prism_utils import seed_id


def run_cell_nexus_simulation():
    prism_dna = seed_id()
    cell = PrismCell(seed=prism_dna)
    return cell.dna == prism_dna


def run_prism_nexus_simulation():
    run_cell_nexus_simulation()


def run_drone_nexus_simulation():
    nexus_engine = NexusEngine(uuid.uuid4())
    run_engine_simulation(nexus_engine)


def run_nexus_simulations():
    run_prism_nexus_simulation()
    run_drone_nexus_simulation()


"""

TODO: Finish this first in nexus_mechanics.py
Library	Purpose	Key Features
NumPy (numpy)	General numerical operations arrays, vectors, matrix multiplications
SymPy (sympy)	Symbolic tensor calculus differentiation, integrals, tensor algebra
SciPy (scipy)	Solving tensor-based physics problems ODE&PDE solvers, numerical integration?
PyTorch (torch)	High-performance tensor computations Automatic differentiation, optimized matrix operations

"""

