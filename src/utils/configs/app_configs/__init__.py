from uuid import UUID

from src.utils.configs import Config
from src.utils.enums.platform_enums import PlatformType


class AppConfig(Config):
    app_id: UUID
    platform: PlatformType

