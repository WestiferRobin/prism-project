from uuid import UUID

from src.utils.configs import Config
from src.utils.configs.app_configs import AppConfig
from src.utils.configs.app_configs.game_config import GameConfig


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

    return True


def validate_app_config(
    source_config: AppConfig,
    target_config: AppConfig,
    ignore_id: bool = True,
    ignore_name: bool = True
) -> bool:
    assert isinstance(source_config, AppConfig)

    assert source_config.platform_type == target_config.platform_type
    assert len(source_config.accounts) == len(target_config.accounts)

    assert validate_config(
        source_config=source_config,
        target_config=target_config,
        ignore_id=ignore_id,
        ignore_name=ignore_name
    )

    return True


def validate_game_config(
    source_config: GameConfig,
    target_config: GameConfig,
    ignore_id: bool = True,
    ignore_name: bool = True
) -> bool:
    assert isinstance(source_config, GameConfig)
    assert validate_app_config(
        source_config=source_config,
        target_config=target_config,
        ignore_id=ignore_id,
        ignore_name=ignore_name
    )

    return True

