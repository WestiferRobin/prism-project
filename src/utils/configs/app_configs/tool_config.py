from typing import List
from uuid import UUID

from src.utils.configs.app_configs import AppConfig
from src.utils.configs.model_configs.account_config import AccountConfig


class ToolConfig(AppConfig):
    def __init__(self,
        tool_id: UUID,
        account_configs: List[AccountConfig],
        **tool_data
    ) -> None:
        super().__init__(
            app_id=tool_id,
            account_configs=account_configs,
            **tool_data
        )

