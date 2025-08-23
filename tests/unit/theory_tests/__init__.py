from src.api.builders.model_builders.game_builders.faction_builder import build_faction
from src.models.prisms import Prism
from src.utils.configs.model_configs.prism_config import PrismConfig


def test_monotheism_history(admin: PrismConfig, emporer: Prism):
    lion_legion = build_faction()

