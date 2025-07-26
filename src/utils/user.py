from src.models.prisms import Prism
from src.utils.configs.model_configs.prism_config import PrismConfig


class User(Prism):
    def __init__(self, config: PrismConfig, **prism_data):
        super().__init__(config=config, prism_data=prism_data)

