from src.app.models.app_models.prisms import Prism
from zlegacy.app.models import Shuttle
from src.app.models.app_models.vehicles.speeder import Speeder


def validate_legion_drone(drone: Prism):
    assert isinstance(drone, Prism)


def validate_legion_speeder(speeder: Speeder):
    assert isinstance(speeder, Speeder)


def validate_legion_shuttle(shuttle: Shuttle):
    assert isinstance(shuttle, Shuttle)


def validate_arch_legion(legion: Legion):
    assert isinstance(legion, Legion)


def validate_nexus_labs(lab: Tool):
    assert isinstance(lab, Tool)


def validate_solar_conquest(game: Game):
    assert isinstance(game, Game)


def validate_prism_forge(forge: App):
    assert isinstance(forge, App)




