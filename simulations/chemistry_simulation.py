from src.chemistry.reactions import hydrogen_combustion
from src.utils.exceptions import VersionException

def hydrogen_test():
    print("Running Hydrogen Combustion Simulation...")

    # Set up molecules
    initial_reactants = {
        "H2": 4,  # 4 H2 molecules
        "O2": 2   # 2 O2 molecules
    }

    result = hydrogen_combustion(initial_reactants)

    print("=== Results ===")
    for molecule, count in result.items():
        print(f"{molecule}: {count}")



def run_chemistry_simulation(version: int):
    if version == 0:
        hydrogen_test()
    else:
        raise VersionException(0, version)
