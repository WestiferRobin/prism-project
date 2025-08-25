from uuid import UUID

from src.utils.configs.app_configs.terminal_configs import TerminalConfig
from src.utils.enums.platform_enums import PlatformType


class WebConfig(TerminalConfig):
    def __init__(self, version: int, web_id: UUID = None, platform_type: PlatformType = PlatformType.Web):
        super().__init__(
            version=version,
            platform_type=platform_type,
            terminal_id=web_id
        )

    @property
    def web_id(self) -> UUID:
        return self.terminal_id



