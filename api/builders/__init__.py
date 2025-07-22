from uuid import uuid4

from api.builders.prism_builder import build_prism
from api.builders.vehicle_builder import build_speeder
from app.models.prisms import Prism
from app.models.simulations.games.solar_conquest import SolarConquest
from app.models.vehicles.speeder import Speeder
from utils.exceptions import NexusException
from utils.version import Version


def build_prism_drone(version: Version) -> Prism:
    prism_drone = build_prism(dna=uuid4())
    return prism_drone


def build_legion_speeder(version: Version) -> Speeder:
    legion_speeder = build_speeder()
    return legion_speeder


def build_arch_legion(version: Version) -> Legion:
    legion = build_legion()
    return legion


def build_solar_conquest(version: Version) -> Game:
    solar_conquest = build_game()
    return solar_conquest


def build_nexus_labs(version: Version) -> Tool:
    nexus_labs = build_app(alias="nexus-labs")
    return nexus_labs


def build_prism_forge(version: Version) -> App:
    prism_forge = build_app(alias="prism-forge")
    return prism_forge
