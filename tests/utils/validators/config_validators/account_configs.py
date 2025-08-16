from utils.validators.config_validators import validate_config
from src.utils.configs.model_configs.account_config import AccountConfig


def validate_account_config(source_config: AccountConfig, target_config: AccountConfig):
    assert source_config is not None
    assert isinstance(source_config, AccountConfig)
    validate_config(
        source_config=source_config,
        target_config=target_config
    )

