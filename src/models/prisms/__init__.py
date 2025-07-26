from pydantic import BaseModel

from src.utils.configs.model_configs.prism_config import PrismConfig


class Prism(BaseModel):
    config: PrismConfig


