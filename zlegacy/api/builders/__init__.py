from uuid import uuid4, UUID

from zlegacy.api.builders.prism_builder import build_prism
from zlegacy.api.builders.vehicle_builder import build_speeder, build_shuttle
from src.prism_net import Mvp
from zlegacy.app.models.app_models.prisms import Prism
from zlegacy.app.models import Shuttle
from zlegacy.app.models.app_models.vehicles.speeder import Speeder


def build_prism_mvp(version: int) -> Mvp:
    return Mvp(version=version)


def build_legion_drone(drone_id: UUID = None) -> Prism:
    if drone_id is None:
        drone_id = uuid4()
    prism_drone = build_prism(dna=drone_id)
    return prism_drone


def build_legion_speeder(pilot_id: UUID = None) -> Speeder:
    if pilot_id is None:
        pilot_id = uuid4()
    pilot = build_legion_drone(pilot_id)
    legion_speeder = build_speeder(pilot=pilot)
    return legion_speeder


def build_legion_shuttle(pilot_id: UUID = None, co_pilot_id: UUID = None) -> Shuttle:
    if pilot_id is None:
        pilot_id = uuid4()
    if co_pilot_id is None:
        co_pilot_id = uuid4()
    pilot = build_legion_drone(pilot_id)
    co_pilot = build_legion_drone(co_pilot_id)
    legion_shuttle = build_shuttle(pilot=pilot, co_pilot=co_pilot)
    return legion_shuttle


def build_arch_legion(admin_id: UUID = None) -> Legion:
    if admin_id is None:
        admin_id = uuid4()
    admin = build_legion_drone(admin_id)
    legion = build_legion(admin=admin)
    return legion


def build_solar_conquest(owner_id: UUID = None) -> Game:
    if owner_id is None:
        owner_id = uuid4()
    solar_conquest = build_game(owner_id=owner_id)
    return solar_conquest


def build_nexus_labs(user_id: UUID = None) -> Tool:
    if user_id is None:
        user_id = uuid4()
    nexus_labs = build_app(alias="nexus-labs")
    nexus_labs.register_user(user_id=user_id)
    return nexus_labs


def build_prism_forge(user_id: UUID = None) -> App:
    if user_id is None:
        user_id = uuid4()
    prism_forge = build_app(alias="prism-forge")
    prism_forge.register_app(user_id=user_id)
    return prism_forge
