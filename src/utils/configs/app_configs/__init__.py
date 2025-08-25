from typing import Dict, List
from uuid import UUID

from src.utils.configs import Config
from src.utils.configs.app_configs.terminal_configs import TerminalConfig
from src.utils.configs.model_configs.account_config import AccountConfig
from src.utils.enums.platform_enums import PlatformType, AppType


class AppConfig(Config):
    terminal_config: TerminalConfig
    accounts: Dict[UUID, AccountConfig]
    app_type: AppType

    @property
    def account_configs(self) -> List[AccountConfig]:
        return list(self.accounts.values())

    @property
    def app_id(self) -> UUID:
        return self.id

    @property
    def terminal_id(self) -> UUID:
        return self.terminal_config.terminal_id

    @property
    def platform_type(self) -> PlatformType:
        return self.platform_config.platform_type

    def __init__(self,
        account_configs: List[AccountConfig],
        app_id: UUID = None,
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

