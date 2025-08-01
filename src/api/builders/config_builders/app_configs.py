from typing import List
from uuid import UUID, uuid4

from src.utils.configs.app_configs import AppConfig
from src.utils.configs.app_configs.game_config import GameConfig
from src.utils.configs.app_configs.tool_config import ToolConfig
from src.utils.configs.model_configs.account_config import AccountConfig
from src.utils.enums.game_enums import GameMode
from src.utils.enums.platform_enums import PlatformType


def build_app_config(
    version: int,
    app_name: str,
    app_alias: str,
    platform: PlatformType,
    app_id: UUID = None,
    account_configs: List[AccountConfig] = None,
) -> AppConfig:
    if app_id is None:
        app_id = uuid4()
    if account_configs is None:
        account_configs = []
    return AppConfig(
        version=version,
        app_id=app_id,
        name=app_name,
        alias=app_alias,
        platform=platform,
        account_configs=account_configs,
    )


def build_game_config(
    version: int,
    game_name: str,
    game_alias: str,
    game_mode: GameMode,
    platform: PlatformType,
    game_id: UUID = None,
    player_configs: List[AccountConfig] = None,
) -> GameConfig:
    if game_id is None:
        game_id = uuid4()
    app_config = build_app_config(
        version=version,
        app_id=game_id,
        app_name=game_name,
        app_alias=game_alias,
        platform=platform,
        account_configs=player_configs
    )
    return GameConfig(
        version=version,
        game_id=app_config.id,
        name=app_config.name,
        alias=app_config.alias,
        mode=game_mode,
        player_configs=app_config.account_configs,
        platform=app_config.platform
    )


def build_tool_config(
    version: int,
    tool_name: str,
    tool_alias: str,
    platform: PlatformType,
    tool_id: UUID = None,
    account_configs: List[AccountConfig] = None
) -> ToolConfig:
    if tool_id is None:
        tool_id = uuid4()
    app_config = build_app_config(
        version=version,
        app_id=tool_id,
        app_name=tool_name,
        app_alias=tool_alias,
        platform=platform,
        account_configs=account_configs
    )
    return ToolConfig(
        version=app_config.version,
        tool_id=app_config.id,
        name=app_config.name,
        alias=app_config.alias,
        platform=app_config.platform,
        account_configs=app_config.account_configs,
    )

