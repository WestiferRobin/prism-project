from src.models.molecule import Molecule


def total_mass(side: dict[Molecule, int]) -> float:
    return sum(mol.mass() * count for mol, count in side.items())
