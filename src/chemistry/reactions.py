from src.models.molecule import Molecule
from src.models.reaction import Reaction
from src.utils.exceptions.chemistry_exceptions.reaction_exceptions import ReactionUnbalanceException


def create_reaction(
        reactants: dict[Molecule, int],
        products: dict[Molecule, int],
        reaction_type: str=None
) -> Reaction:
    """
    General reaction constructor with balance validation.
    """
    reaction = Reaction(reactants=reactants, products=products)
    if not reaction.is_balanced():
        raise ReactionUnbalanceException(reaction)
    if reaction_type:
        reaction.type = reaction_type
    return reaction


def create_synthesis_reaction(
        reactants: dict[Molecule, int],
        product: tuple[Molecule, int]
) -> Reaction:
    """
    A + B → AB
    """
    return create_reaction(
        reactants=reactants,
        products={product[0]: product[1]},
        reaction_type="synthesis"
    )


def create_decomposition_reaction(
        reactant: tuple[Molecule, int],
        products: dict[Molecule, int]
) -> Reaction:
    """
    AB → A + B
    """
    return create_reaction(
        reactants={reactant[0]: reactant[1]},
        products=products,
        reaction_type="decomposition"
    )


def create_single_replacement_reaction(
        reactants: dict[Molecule, int],
        products: dict[Molecule, int]
) -> Reaction:
    """
    AB + C → AC + B
    """
    return create_reaction(
        reactants=reactants,
        products=products,
        reaction_type="single_replacement"
    )


def create_double_replacement_reaction(
        reactants: dict[Molecule, int],
        products: dict[Molecule, int]
) -> Reaction:
    """
    AB + CD → AD + CB
    """
    return create_reaction(
        reactants=reactants,
        products=products,
        reaction_type="double_replacement"
    )
