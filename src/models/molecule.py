from src.chemistry.atoms import get_atom_by_symbol
from src.models.atom import Atom


class Molecule:
    def __init__(self, name: str, elements: list[Atom]):
        self.name = name
        self.elements = elements  # {'H': 2, 'O': 1}

    def __str__(self):
        return f"{self.name} at {self.mass()} g/mol"

    # Molecule mass is molar_mass (g/mol)
    def mass(self):
        count_table = {}
        atom_table = {}
        for element in self.elements:
            symbol = element.symbol
            if symbol not in atom_table:
                atom_table[symbol] = element
            if symbol in count_table:
                count_table[symbol] += 1
            else:
                count_table[symbol] = 1

        total = 0
        for symbol in atom_table:
            count = count_table[symbol]
            atomic_mass = atom_table[symbol].atomic_mass
            total += count * atomic_mass

        return total

if __name__ == "__main__":
    water_atoms = [
        get_atom_by_symbol('H'),
        get_atom_by_symbol('H'),
        get_atom_by_symbol('O')
    ]
    formula = "H20"
    water_molecule = Molecule(name=formula, elements=water_atoms)
    molecule_mass = water_molecule.mass()
    print(water_molecule.name, molecule_mass)