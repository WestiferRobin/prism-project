from src.utils.exceptions.simulation_exceptions import SimulationException
from src.utils.periodic_table import PERIODIC_TABLE


def run_atom_simulation():
    atomic_symbols = []
    for atom in PERIODIC_TABLE.values():
        if atom.symbol in atomic_symbols:
            raise SimulationException(f"{atom.symbol} is already found for run_atom_simulation.")
        atomic_symbols.append(atom.symbol)
