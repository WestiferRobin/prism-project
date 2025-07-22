from uuid import UUID

from src.api.builders import build_prism_mvp
from src.api.validators import validate_arch_legion, validate_nexus_labs, validate_solar_conquest, validate_prism_forge, \
    validate_legion_drone, validate_legion_speeder, validate_legion_shuttle
from src.mvp import PrismMvp


def test_prism_mvp(version: int):
    user_id = UUID("00000000-0000-0000-0000-000000000000")
    prism_mvp = build_prism_mvp(version=version, user_id=user_id)
    assert prism_mvp.version >= 0
    assert isinstance(prism_mvp, PrismMvp)

    # Alpha Tests: Models to App
    validate_legion_drone(prism_mvp.legion_drone)
    validate_legion_speeder(prism_mvp.legion_speeder)
    validate_legion_shuttle(prism_mvp.legion_shuttle)
    validate_arch_legion(prism_mvp.arch_legion)

    # Beta Tests: Models to Specific Apps
    validate_solar_conquest(prism_mvp.solar_conquest)
    validate_nexus_labs(prism_mvp.nexus_labs)

    # Gamma Tests: Models to General Apps
    validate_prism_forge(prism_mvp.prism_forge)
    validate_prism_studio(prism_mvp.prism_studio)
    validate_prism_hive(prism_mvp.prism_hive)

