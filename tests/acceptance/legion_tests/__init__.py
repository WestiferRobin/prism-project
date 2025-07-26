from src.utils.enums.game_enums.faction_enums import FactionType


def test_faction_legion():
    for faction_type in FactionType:
        faction = build_faction(faction_type=faction_type)

