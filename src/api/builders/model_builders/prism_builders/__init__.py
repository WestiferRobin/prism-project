from src.utils.configs.model_configs.prism_config import PrismConfig
from src.models.prisms import Prism


def build_prism(config: PrismConfig) -> Prism:
    return Prism(config=config)

