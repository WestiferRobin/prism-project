from src.api.validators.config_validators.server_configs import validate_server_config
from src.models.drones import Drone
from src.models.hive_server import HiveServer
from src.utils.configs.bot_configs.server_config import ServerConfig


def validate_hive_server(server: HiveServer):
    assert server is not None
    assert isinstance(server, HiveServer)

    assert server.config is not None
    assert isinstance(server.config, ServerConfig)
    validate_server_config(config=server.config)

    assert server.drone is not None
    assert isinstance(server.drone, Drone)



