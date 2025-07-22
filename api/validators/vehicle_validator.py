from api.validators.config_validator import validate_vehicle_config
from utils.enums import VehicleType
from app.models.equations.chemistry.mass import Mass
from app.models.vehicles import Vehicle
from app.models.vehicles.shuttle import Shuttle
from app.models.vehicles.speeder import Speeder


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

