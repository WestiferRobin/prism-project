from src.models.atom import Atom


class Molecule:
    def __init__(self, name: str, elements: list[Atom]):
        self.name = name
        self.elements = elements  # {'H': 2, 'O': 1}

    def __str__(self):
        breakdown = {}
        for atom in self.elements:
            breakdown[atom.symbol] = breakdown.get(atom.symbol, 0) + 1
        breakdown_str = ''.join(f"{k}{v if v > 1 else ''}" for k, v in sorted(breakdown.items()))
        return f"{breakdown_str} at {self.mass():.3f} g/mol"

    # Molecule mass is molar_mass (g/mol)
    def mass(self) -> float:
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
