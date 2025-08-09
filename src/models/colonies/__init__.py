from pydantic import BaseModel

from src.utils.configs.model_configs.colony_config import ColonyConfig


class Colony(BaseModel):
    colony_config: ColonyConfig

