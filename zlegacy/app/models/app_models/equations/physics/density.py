from zlegacy.app.models import Equation
from zlegacy.app.models.app_models.equations.chemistry.mass import Mass
from zlegacy.app.models.app_models.unit import Unit


class Density(Unit):
    mass: Mass
    volume: Equation

    def __init__(self, **density_data):
        super().__init__(**density_data)

