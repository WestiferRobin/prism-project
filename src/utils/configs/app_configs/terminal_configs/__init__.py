from uuid import UUID

from src.utils.configs import Config
from src.utils.enums.platform_enums import PlatformType


class TerminalConfig(Config):
    platform_type: PlatformType

    def __init__(self,
        version: int,
        platform_type: PlatformType = PlatformType.Terminal,
        terminal_id: UUID = None
    ):
        super().__init__(
            version=version,
            config_id=terminal_id,
            name=platform_type.name,
            alias=platform_type.name.lower(),
            platform_type=platform_type
        )

    @property
    def terminal_id(self) -> UUID:
        return self.id

