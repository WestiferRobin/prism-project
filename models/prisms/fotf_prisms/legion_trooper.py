from configs.prism_config import PrismConfig
from models.prisms.model import PrismDrone


class LegionTrooper(PrismDrone):
    def __init__(self, config: PrismConfig):
        super().__init__(config)
