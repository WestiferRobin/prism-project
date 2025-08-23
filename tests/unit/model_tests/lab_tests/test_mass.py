from typing import List, Dict

from pydantic import BaseModel

from src.api.builders.model_builders.lab_builders.density_builders import build_water_density
from src.api.builders.model_builders.lab_builders.mass_builder import build_mass
from src.api.builders.model_builders.lab_builders.volume_builder import build_cube_volume
from src.models.equations.chemistry.atom import Atom
from src.models.equations.chemistry.density import Density
from src.models.equations.chemistry.molecule import Molecule
from src.models.equations.math import Position
from src.models.equations.math.volume import Volume
from src.utils.constants.science_constants import PERIODIC_TABLE
from utils.validators.model_validators.mass_validator import validate_mass


def build_atom(name: str, charge: float = 0) -> Atom:
    names = set()
    for element in PERIODIC_TABLE["elements"]:
        names.add(element["name"].lower())
    if name.lower() not in names:
        raise ValueError(f"{name} not in {PERIODIC_TABLE['elements']}")
    atom_data = PERIODIC_TABLE[name.lower()]
    return Atom(
        number=atom_data["number"],
        symbol=atom_data["symbol"],

        period=atom_data["period"],
        group=atom_data["group"],
        name=atom_data["name"],
        description=atom_data["appearance"],
        atomic_mass=atom_data["atomic_mass"],

        density=atom_data["density"],
        boil_point=atom_data["boil_point"],
        melt_point=atom_data["melt_point"],
        molar_heat=atom_data["molar_heat"],

        position=Position(
            x=atom_data["xpos"],
            y=atom_data["ypos"],
            z=atom_data["wxpos"],
            w=atom_data["wypos"]
        ),
        shells=atom_data["shells"],
        electron_configuration=atom_data["electron_configuration"],
        charge=charge
    )


def build_molecule(equation: str, name: str, atoms: List[Atom]) -> Molecule:
    return Molecule(
        equation=equation,
        name=name,
        atoms=atoms
    )


def test_atom(name: str = "Hydrogen"):
    atom = build_atom(name=name)
    assert validate_atom(atom=atom)


def test_molecule(equation: str, description: str):
    molecule = build_molecule(
        equation=equation,
        description=description
    )


def test_water_molecule():
    equation = "H20"
    description = "water"
    test_molecule(
        equation=equation,
        description=description
    )


def test_mass(volume: Volume = None, density: Density = None):
    if volume is None:
        volume = build_cube_volume(length=1)
    if density is None:
        density = build_water_density(amount=1)
    mass = build_mass(volume=volume, density=density)
    assert validate_mass(mass=mass)

