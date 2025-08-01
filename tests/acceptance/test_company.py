from src.api.builders.config_builders.user_configs.wes_config import build_wes_config
from src.utils.constants import DEBUG_VERSION


def test_prism_co():
    leader_config = build_wes_config(version=DEBUG_VERSION)

