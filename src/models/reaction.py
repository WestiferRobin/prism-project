from src.models.molecule import Molecule
from src.utils.mass_utils import total_mass
from src.utils.reaction_utils import count_atoms, format_reaction


class Reaction:
    def __init__(self, reactants: dict[Molecule, int], products: dict[Molecule, int], reaction_type: str = "Unknown"):
        self.reactants = reactants
        self.products = products
        self.type = reaction_type

    def __str__(self):
        return f"{format_reaction(self.reactants)} -> {format_reaction(self.products)}"

    def is_balanced(self) -> bool:
        return count_atoms(self.reactants) == count_atoms(self.products)

    def mass_reactants(self) -> float:
        return total_mass(side=self.reactants)

    def mass_products(self) -> float:
        return total_mass(side=self.products)
