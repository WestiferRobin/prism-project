from src.utils.configs import Config


def validate_config(config: Config):
    assert config is not None
    assert isinstance(config, Config)

    assert config.version is not None
    assert isinstance(config.version, int)
    assert config.version >= 0

    assert config.name is not None
    assert isinstance(config.name, str)

    assert config.alias is not None
    assert isinstance(config.alias, str)

