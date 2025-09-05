from src.api.builders.config_builders.user_configs.wes_config import build_wes_config
from src.company import Company


def build_mvp(version: int) -> Company:
    return build_prism_co(
        version=version,
        leader_config=build_wes_config(version=version)
    )

