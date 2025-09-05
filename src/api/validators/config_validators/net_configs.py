from src.api.validators.config_validators import validate_config
from src.utils.configs.net_config import NetConfig


def validate_net_config(source_config: NetConfig, target_config: NetConfig):
    assert source_config is not None
    assert isinstance(source_config, NetConfig)
    validate_config(
        source_config=source_config,
        target_config=target_config
    )

    assert len(source_config.user_configs) == len(target_config.user_configs)
    assert len(source_config.app_configs) == len(target_config.app_configs)
    assert len(source_config.bot_configs) == len(target_config.bot_configs)

