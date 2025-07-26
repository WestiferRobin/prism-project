import uuid
from uuid import UUID

from src.utils.configs.app_configs import AppConfig
from src.utils.enums.platform_enums import PlatformType


class GameConfig(AppConfig):
    game_id: UUID
    platform: PlatformType

    def __init__(self,
        name: str,
        platform: PlatformType,
        game_id: UUID = None,
        app_id: UUID = None,
        **game_data
    ) -> None:
        if game_id is None:
            game_id = uuid.uuid4()
        if app_id is None:
            app_id = game_id
        super().__init__(
            name=name,
            platform=platform,
            app_id=app_id,
            game_id=game_id,
            **game_data
        )

