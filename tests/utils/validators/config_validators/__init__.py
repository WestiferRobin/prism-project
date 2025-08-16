from uuid import UUID

from src.utils.configs import Config


def validate_config(
    source_config: Config,
    target_config: Config,
    ignore_id: bool = True,
    ignore_name: bool = True
):
    assert source_config is not None
    assert isinstance(source_config, Config)

    assert source_config.version is not None
    assert isinstance(source_config.version, int)
    assert source_config.version == target_config.version

    assert source_config.id is not None
    assert isinstance(source_config.id, UUID)
    if not ignore_id:
        assert source_config.id == target_config.id

    assert source_config.name is not None
    assert isinstance(source_config.name, str)
    if not ignore_name:
        assert source_config.name.lower() == target_config.name.lower()

    assert source_config.alias is not None
    assert isinstance(source_config.alias, str)
    if not ignore_name:
        assert source_config.alias.lower() == target_config.alias.lower()

