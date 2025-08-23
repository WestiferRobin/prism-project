from typing import List

from pydantic import BaseModel

from src.models.equations.chemistry.atom import Atom


class Molecule(BaseModel):
    equation: str
    name: str
    atoms: List[Atom]

