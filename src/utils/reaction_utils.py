from src.models.molecule import Molecule


def count_atoms(molecules: dict[Molecule, int]) -> dict[str, int]:
    total: dict[str, int] = {}
    for molecule, count in molecules.items():
        for atom in molecule.elements:
            symbol = atom.identity.symbol
            if symbol not in total:
                total[symbol] = 0
            total[symbol] += count
    return total

def format_reaction(molecules: dict[Molecule, int]) -> str:
    parts = []
    for mol, count in molecules.items():
        label = mol.name
        parts.append(f"{count} {label}" if count > 1 else label)
    return ' + '.join(parts)