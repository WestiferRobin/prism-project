from uuid import uuid4

from src.api.builders.config_builders.drone_configs.leader_configs import build_leader_config
from src.utils.configs.company_config import CompanyConfig
from src.utils.configs.model_configs.user_config import UserConfig
from src.utils.enums.prism_enums import RankType, RaceType


def build_company_config(
    version: int,
    company_name: str,
    company_alias: str,
    leader_config: UserConfig
) -> CompanyConfig:
    tech_officer = build_leader_config(
        version=version,
        rank=RankType.Arch,
        leader_race=RaceType.Human
    )
    market_officer = build_leader_config(
        version=version,
        rank=RankType.Arch,
        leader_race=RaceType.Human
    )

    company_config = CompanyConfig(
        version=version,
        config_id=uuid4(),
        name=company_name,
        alias=company_alias,

        leader_config=leader_config,
        tech_leader_config=tech_officer,
        market_leader_config=market_officer
    )
    return company_config

