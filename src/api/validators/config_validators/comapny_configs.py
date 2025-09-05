from src.api.validators.config_validators.legion_configs import validate_legion_config
from src.api.validators.config_validators.user_configs import validate_user_config
from src.utils.configs.company_config import CompanyConfig
from src.utils.configs.model_configs.user_config import UserConfig


def validate_company_config(source_config: CompanyConfig, target_config: CompanyConfig):
    assert source_config is not None
    assert isinstance(source_config, CompanyConfig)
    validate_legion_config(
        source_config=source_config,
        target_config=target_config
    )

    assert source_config.leader_config is not None
    assert isinstance(source_config.leader_config, UserConfig)
    validate_user_config(
        source_config=source_config.leader_config,
        target_config=target_config.leader_config
    )

