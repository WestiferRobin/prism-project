from src.api.builders.config_builders.drone_configs.leader_configs import build_leader_config
from src.api.builders.config_builders.user_configs import build_payton_config
from src.api.builders.config_builders.user_configs.max_config import build_max_config
from src.api.builders.config_builders.user_configs.tyler_config import build_tyler_config
from src.api.builders.config_builders.user_configs.wes_config import build_wes_config
from src.api.builders.model_builders.faction_builder import build_faction
from src.api.validators.model_validators.legion_validator import validate_legion
from src.utils.configs.model_configs.drone_config import DroneConfig
from src.utils.constants import DEBUG_VERSION
from src.utils.enums.game_enums.faction_enums import FactionType
from src.utils.enums.prism_enums import RankType


def test_faction(
    version: int = DEBUG_VERSION,
    faction_type: FactionType = FactionType.Federation,
    leader_config: DroneConfig = None
):
    if leader_config is None:
        wes_config = build_wes_config(version=version)
        leader_config = wes_config.avatar_config

    faction_legion = build_faction(
        version=version,
        faction_type=faction_type,
        leader_config=leader_config,
        vice_config=build_leader_config(
            version=version,
            rank=RankType.Arch
        ),
        general_config=build_leader_config(
            version=version,
            rank=RankType.Arch
        ),
        admiral_config=build_leader_config(
            version=version,
            rank=RankType.Arch
        )
    )
    validate_legion(legion=faction_legion)


def test_factions(version: int = DEBUG_VERSION):
    for faction_type in FactionType:
        test_faction(version=version, faction_type=faction_type)


def test_classic_mode_factions(version: int = DEBUG_VERSION):
    wes_config = build_wes_config(version=version)
    max_config = build_max_config(version=version)

    test_faction(
        version=version,
        faction_type=FactionType.Federation,
        leader_config=wes_config.avatar_config,
    )
    test_faction(
        version=version,
        faction_type=FactionType.Empire,
        leader_config=max_config.avatar_config
    )


def test_royale_mode_factions(version: int = DEBUG_VERSION):
    test_classic_mode_factions(version=version)

    tyler_config = build_tyler_config(version=version)
    payton_config = build_payton_config(version=version)

    test_faction(
        version=version,
        faction_type=FactionType.Exchange,
        leader_config=tyler_config.avatar_config,
    )
    test_faction(
        version=version,
        faction_type=FactionType.Confederacy,
        leader_config=payton_config.avatar_config,
    )