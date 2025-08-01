from uuid import UUID

from src.utils.configs.app_configs import AppConfig


class ToolConfig(AppConfig):
    def __init__(self, tool_id: UUID, **tool_data) -> None:
        super().__init__(
            app_id=tool_id,
            app_data=tool_data
        )

