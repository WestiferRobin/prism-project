from pydantic import BaseModel

from src.models.equation import Equation
from src.models.mass import Mass
from src.models.unit import Unit


class Density(Unit):
    mass: Mass
    volume: Equation

    def __init__(self, **density_data):
        super().__init__(**density_data)

