from src.utils.configs.bot_configs.server_config import ServerConfig


def validate_server_config(config: ServerConfig):
    assert config is not None
    assert isinstance(config, ServerConfig)

