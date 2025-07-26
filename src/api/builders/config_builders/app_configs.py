from uuid import UUID, uuid4

from src.utils.configs.app_configs import AppConfig
from src.utils.configs.app_configs.game_config import GameConfig
from src.utils.configs.app_configs.tool_config import ToolConfig
from src.utils.enums.platform_enums import PlatformType


def build_app_config(version: int, name: str, alias: str, platform: PlatformType, app_id: UUID = None) -> AppConfig:
    if app_id is None:
        app_id = uuid4()
    return AppConfig(
        version=version,
        alias=alias,
        name=name,
        app_id=app_id,
        platform=platform
    )


def build_game_config(version: int, name: str, alias: str, platform: PlatformType, game_id: UUID = None) -> GameConfig:
    if game_id is None:
        game_id = uuid4()
    return GameConfig(
        version=version,
        alias=alias,
        name=name,
        game_id=game_id,
        platform=platform
    )


def build_tool_config(version: int, name: str, alias: str, platform: PlatformType, tool_id: UUID = None) -> ToolConfig:
    if tool_id is None:
        tool_id = uuid4()
    return ToolConfig(
        version=version,
        alias=alias,
        name=name,
        tool_id=tool_id,
        platform=platform
    )

