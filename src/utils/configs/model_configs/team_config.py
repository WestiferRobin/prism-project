from typing import List

from src.utils.configs import Config
from src.utils.configs.model_configs.drone_config import DroneConfig


class TeamConfig(Config):
    leader_config: DroneConfig
    worker_configs: List[DroneConfig]


