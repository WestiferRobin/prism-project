import uuid
from uuid import UUID

from src.utils.configs.app_configs import AppConfig
from src.utils.enums.platform_enums import PlatformType


class WidgetConfig(AppConfig):
    widget_id: UUID
    platform: PlatformType

    def __init__(self,
        name: str,
        platform: PlatformType,
        widget_id: UUID = None,
        app_id: UUID = None,
        **widget_data
    ) -> None:
        if widget_id is None:
            widget_id = uuid.uuid4()
        if app_id is None:
            app_id = widget_id
        super().__init__(
            name=name,
            platform=platform,
            app_id=app_id,
            widget_id=widget_id,
            app_data=widget_data
        )

