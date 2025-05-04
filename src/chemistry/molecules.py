import re
from src.chemistry.atoms import get_atom_by_symbol
from src.models.atom import Atom
from src.models.molecule import Molecule


def parse_formula(formula: str) -> list[tuple[str, int]]:
    """
    Parses chemical formulas like 'H2O' or 'C6H12O6' into [('H', 2), ('O', 1)]
    """
    pattern = r'([A-Z][a-z]*)(\d*)'
    matches = re.findall(pattern, formula)
    result = []
    for symbol, count in matches:
        amount = int(count) if count else 1
        result.append((symbol, amount))
    return result


def create_molecule(formula: str) -> Molecule:
    elements: list[Atom] = []
    for symbol, count in parse_formula(formula):
        atom = get_atom_by_symbol(symbol)
        if atom:
            elements.extend([atom] * count)
    return Molecule(name=formula, elements=elements)


if __name__ == "__main__":
    water_formula = "H2O"
    compound_formula = "O2"
    complex_formula = "C6H12O6"

    water_molecule = create_molecule(formula=water_formula)
    dioxygen_molecule = create_molecule(formula=compound_formula)
    complex_molecule = create_molecule(formula=complex_formula)

    print(water_molecule)
    print(dioxygen_molecule)
    print(complex_molecule)
