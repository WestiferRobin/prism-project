from typing import Dict, List
from uuid import UUID

from src.utils.configs import Config
from src.utils.configs.model_configs.account_config import AccountConfig
from src.utils.enums.platform_enums import PlatformType


class AppConfig(Config):
    platform: PlatformType
    accounts: Dict[UUID, AccountConfig]

    @property
    def account_configs(self) -> List[AccountConfig]:
        return list(self.accounts.values())

    def __init__(self,
        app_id: UUID,
        account_configs: List[AccountConfig],
        **app_data
    ):
        accounts = {}
        for account_config in account_configs:
            accounts[account_config.id] = account_config
        super().__init__(
            config_id=app_id,
            accounts=accounts,
            **app_data
        )



