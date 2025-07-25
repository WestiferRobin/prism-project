from pydantic import BaseModel

from src.utils.configs.prism_config import PrismConfig


class Prism(BaseModel):
    config: PrismConfig


