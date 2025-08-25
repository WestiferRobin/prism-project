from uuid import UUID

from src.utils.configs.app_configs.terminal_configs.web_config import WebConfig
from src.utils.enums.platform_enums import PlatformType


class MobileConfig(WebConfig):
    def __init__(self, version: int, mobile_id: UUID = None, platform_type: PlatformType = PlatformType.Mobile):
        super().__init__(
            version=version,
            platform_type=PlatformType.Mobile,
            terminal_id=mobile_id
        )

    @property
    def mobile_id(self) -> UUID:
        return self.terminal_id

