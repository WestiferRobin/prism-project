from src.api.validators import validate_config
from src.utils.configs.bot_configs.server_config import ServerConfig


def validate_server_config(config: ServerConfig, expected_value: ServerConfig) -> None:
    assert config is not None
    assert isinstance(config, ServerConfig)

    validate_config(source_config=config, target_config=expected_value)

