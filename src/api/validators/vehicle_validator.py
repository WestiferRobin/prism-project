from src.api.validators.config_validator import validate_vehicle_config
from src.enums import VehicleType
from src.models.mass import Mass
from src.models.vehicles import Vehicle
from src.models.vehicles.shuttle import Shuttle
from src.models.vehicles.speeder import Speeder


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

