from zlegacy.api.validators.config_validator import validate_vehicle_config
from src.utils.enums import VehicleType
from zlegacy.models.app_models import Mass
from zlegacy.models.app_models import Vehicle
from zlegacy.models import Shuttle
from zlegacy.models.app_models import Speeder


def validate_vehicle(vehicle: Vehicle):
    assert vehicle is not None
    assert isinstance(vehicle, Vehicle)

    validate_vehicle_config(vehicle.config)

    assert vehicle.type is not None
    assert isinstance(vehicle.type, VehicleType)

    assert vehicle.mass is not None
    assert isinstance(vehicle.mass, Mass)


def validate_speeder(speeder: Speeder):
    validate_vehicle(speeder)


def validate_shuttle(shuttle: Shuttle):
    validate_vehicle(shuttle)

