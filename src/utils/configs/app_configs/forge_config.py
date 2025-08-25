import uuid
from typing import List
from uuid import UUID

from src.utils.configs.app_configs import AppConfig
from src.utils.configs.model_configs.account_config import AccountConfig
from src.utils.enums.platform_enums import PlatformType


class ForgeConfig(AppConfig):
    platform: PlatformType

    @property
    def forge_accounts(self) -> List[AccountConfig]:
        return self.account_configs

    def __init__(self,
        platform: PlatformType,
        forge_accounts: List[AccountConfig],
        forge_id: UUID = None,
        **widget_data
    ) -> None:
        if forge_id is None:
            forge_id = uuid.uuid4()
        super().__init__(
            platform=platform,
            app_id=forge_id,
            account_configs=forge_accounts,
            app_data=widget_data
        )

