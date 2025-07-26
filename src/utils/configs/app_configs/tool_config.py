import uuid
from uuid import UUID

from src.utils.configs.app_configs import AppConfig
from src.utils.enums.platform_enums import PlatformType


class ToolConfig(AppConfig):
    tool_id: UUID
    platform: PlatformType

    def __init__(self,
        name: str,
        platform: PlatformType,
        tool_id: UUID = None,
        app_id: UUID = None,
        **tool_data
    ) -> None:
        if tool_id is None:
            tool_id = uuid.uuid4()
        if app_id is None:
            app_id = tool_id
        super().__init__(
            name=name,
            platform=platform,
            app_id=app_id,
            tool_id=tool_id,
            **tool_data
        )

