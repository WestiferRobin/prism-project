from typing import List
from uuid import UUID

from src.utils.configs.app_configs import AppConfig
from src.utils.configs.model_configs.user_config import UserConfig


class StudioConfig(AppConfig):
    user_configs: List[UserConfig]

    def __init__(self,
        studio_id: UUID,
        user_configs: List[UserConfig],
        **lab_data
    ) -> None:
        account_configs = []
        for user_config in user_configs:
            for account_config in user_config.account_configs:
                account_configs.append(account_config)
        super().__init__(
            app_id=studio_id,
            account_configs=account_configs,
            user_configs=user_configs,
            **lab_data
        )

    @property
    def studio_id(self) -> UUID:
        return self.app_id

