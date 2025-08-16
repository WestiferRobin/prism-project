from src.utils.configs.model_configs.legion_config import LegionConfig
from src.utils.enums.game_enums.faction_enums import FactionType


class FactionConfig(LegionConfig):
    faction_type: FactionType

    def __init__(self, **faction_data):
        super().__init__(**faction_data)

