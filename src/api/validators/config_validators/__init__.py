from src.utils.configs import Config


def validate_config(
    config: Config,
    expected_value: Config,
):
    assert config is not None
    assert isinstance(config, Config)

    assert config.version is not None
    assert isinstance(config.version, int)
    assert config.version == expected_value.version

    assert config.name is not None
    assert isinstance(config.name, str)
    assert config.name.lower() == expected_value.name.lower()

    assert config.alias is not None
    assert isinstance(config.alias, str)
    assert config.alias.lower() == expected_value.alias.lower()

