import uuid

from src.models.vehicles.model import NexusEngine
from src.simulations.engine_simulations import run_engine_simulation


def simulate_prism_cell():
    cell = []
    for i in range(0, 16):
        for j in range(0, 16):
            cell.append((i, j))
    print(cell)


def run_nexus_simulation():
    nexus_engine = NexusEngine(uuid.uuid4())
    run_engine_simulation(nexus_engine)

"""

TODO: Finish this first in nexus_mechanics.py
Library	Purpose	Key Features
NumPy (numpy)	General numerical operations arrays, vectors, matrix multiplications
SymPy (sympy)	Symbolic tensor calculus differentiation, integrals, tensor algebra
SciPy (scipy)	Solving tensor-based physics problems ODE&PDE solvers, numerical integration?
PyTorch (torch)	High-performance tensor computations Automatic differentiation, optimized matrix operations

"""

