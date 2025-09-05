from src.api.validators.config_validators import validate_config
from src.api.validators.config_validators.account_configs import validate_account_config
from src.api.validators.config_validators.drone_configs import validate_drone_config
from src.utils.configs.model_configs.drone_config import DroneConfig
from src.utils.configs.model_configs.user_config import UserConfig


def validate_user_config(source_config: UserConfig, target_config: UserConfig):
    assert source_config is not None
    assert isinstance(source_config, UserConfig)
    validate_config(
        source_config=source_config,
        target_config=target_config
    )

    assert source_config.avatar_config is not None
    assert isinstance(source_config.avatar_config, DroneConfig)

    validate_drone_config(
        source_config=source_config.avatar_config,
        target_config=target_config.avatar_config
    )
    validate_drone_config(
        source_config=source_config.companion_config,
        target_config=target_config.companion_config
    )

    source_configs = source_config.account_configs
    target_configs = target_config.account_configs
    assert len(source_configs) == len(target_configs)

    for index in range(len(source_configs)):
        validate_account_config(
            source_config=source_configs[index],
            target_config=target_configs[index]
        )

