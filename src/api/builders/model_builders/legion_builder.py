from src.api.builders.model_builders.prism_builders import build_prism
from src.models.prisms import Prism
from src.models.legion import Legion
from src.utils.enums.game_enums.faction_enums import FactionType
from src.utils.enums.prism_enums import RankType


def build_legion(admin: Prism) -> Legion:
    admin.config.rank = RankType.Arch
    return Legion(admin=admin)


def build_faction_legion(faction: FactionType) -> Legion:
    admin_config = build_admin_config(faction=faction)
    faction_admin = build_prism(config=admin_config)
    return build_legion(admin=faction_admin)


