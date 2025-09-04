from typing import List

from src.utils.configs.app_configs import AppConfig
from src.utils.configs.model_configs.drone_config import DroneConfig
from src.utils.configs.model_configs.legion_config import LegionConfig
from src.utils.configs.model_configs.team_config import TeamConfig
from src.utils.configs.model_configs.user_config import UserConfig


class CompanyConfig(LegionConfig):
    leader_config: UserConfig
    chief_configs: List[DroneConfig]
    team_configs: List[TeamConfig]

    game_config: AppConfig
    studio_config: AppConfig

    def __init__(self,
        leader_config: UserConfig,
        tech_leader_config: DroneConfig,
        market_leader_config: DroneConfig,
        **company_data
    ):
        super().__init__(
            leader_config=leader_config,
            admin_config=leader_config.avatar_config,
            vice_config=leader_config.companion_config,
            general_config=tech_leader_config,
            admiral_config=market_leader_config,
            **company_data
        )


