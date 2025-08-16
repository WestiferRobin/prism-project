from src.api import build_user
from src.api.builders import build_hedron_hive
from src.api.builders.config_builders.user_configs import build_user_config
from utils.validators.config_validators.server_configs import validate_server_config
from src.bots import HedronServer
from src.utils.configs.bot_configs.server_config import ServerConfig
from src.utils.user import User


def validate_server(server: HedronServer, version: int) -> None:
    assert server is not None
    assert isinstance(server, HedronServer)
    assert server.version == version

    assert server.config is not None
    assert isinstance(server.config, ServerConfig)

    expected_value = build_hedron_hive(version=version)
    validate_server_config(config=server.config, expected_value=expected_value.config)

    assert server.user is not None
    assert isinstance(server.user, User)

    expected_value = build_user(
        config=build_user_config(,
    )
    validate_user(user=server.user, expected_value=expected_value)



