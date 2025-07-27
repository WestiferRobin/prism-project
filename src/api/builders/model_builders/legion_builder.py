from src.api.builders.model_builders.drone_builder import build_legion_drone
from src.models.drones.legion_drone import LegionDrone
from src.models.legion import Legion
from src.utils.enums.prism_enums import RankType


def build_legion(version: int, admin: LegionDrone = None) -> Legion:
    if admin is None:
        admin = build_legion_drone(version=version, rank=RankType.Arch)

    vice = build_legion_drone(version=version, rank=RankType.Arch)
    general = build_legion_drone(version=version, rank=RankType.Arch)
    admiral = build_legion_drone(version=version, rank=RankType.Arch)

    return Legion(
        admin=admin,
        vice=vice,
        general=general,
        admiral=admiral
    )

