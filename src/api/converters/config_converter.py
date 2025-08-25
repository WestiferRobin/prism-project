from src.api.builders.config_builders.account_configs import build_account_config
from src.utils.configs.model_configs.account_config import AccountConfig
from src.utils.configs.model_configs.user_config import UserConfig


def convert_user_to_account_configs(user_config: UserConfig) -> AccountConfig:
    return [
        build_account_config()

    )

