from src.api.validators.config_validators import validate_config
from src.api.validators.config_validators.drone_configs import validate_drone_config
from src.utils.configs.company_config import CompanyConfig
from src.utils.configs.model_configs.drone_config import DroneConfig
from src.utils.configs.model_configs.legion_config import LegionConfig


def validate_legion_config(
    source_config: LegionConfig,
    target_config: LegionConfig
):
    assert source_config is not None
    assert isinstance(source_config, LegionConfig)
    validate_config(
        source_config=source_config,
        target_config=target_config
    )

    assert source_config.admin_config is not None
    assert isinstance(source_config.admin_config, DroneConfig)
    validate_drone_config(
        source_config=source_config.admin_config,
        target_config=target_config.admin_config
    )

    assert source_config.vice_config is not None
    assert isinstance(source_config.vice_config, DroneConfig)
    validate_drone_config(
        source_config=source_config.vice_config,
        target_config=target_config.vice_config
    )

    assert source_config.general_config is not None
    validate_drone_config(
        source_config=source_config.general_config,
        target_config=target_config.general_config
    )

    assert source_config.admiral_config is not None
    validate_drone_config(
        source_config=source_config.admiral_config,
        target_config=target_config.admiral_config
    )

