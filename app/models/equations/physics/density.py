from app.models.equation import Equation
from app.models.equations.chemistry.mass import Mass
from app.models.unit import Unit


class Density(Unit):
    mass: Mass
    volume: Equation

    def __init__(self, **density_data):
        super().__init__(**density_data)

