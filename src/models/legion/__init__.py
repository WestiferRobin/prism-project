from pydantic import BaseModel

from src.utils.configs.model_configs.legion_config import LegionConfig


class Legion(BaseModel):
    config: LegionConfig

