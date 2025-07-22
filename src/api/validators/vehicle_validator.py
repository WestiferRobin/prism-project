from src.api.validators.config_validator import validate_vehicle_config
from src.utils.enums import VehicleType
from src.app.models.app_models.equations.chemistry.mass import Mass
from src.app.models.app_models.vehicles import Vehicle
from zlegacy.app.models import Shuttle
from src.app.models.app_models.vehicles.speeder import Speeder


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

