from src.api.builders.config_builders.legion_configs.company_configs import build_company_config
from src.api.helpers.alias_helper import configure_alias
from src.company import Company
from src.utils.configs.model_configs.user_config import UserConfig


def build_company(
    version: int,
    company_name: str,
    leader_config: UserConfig
) -> Company:
    company_config = build_company_config(
        version=version,
        company_name=company_name,
        company_alias=configure_alias(company_name),
        leader_config=leader_config,
    )
    return Company(config=company_config)


def build_prism_co(
    version: int,
    leader_config: UserConfig
) -> Company:
    return build_company(
        version=version,
        company_name="Prism Co",
        leader_config=leader_config,
    )

