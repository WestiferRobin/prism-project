from src.api.builders.prism_builders import build_prism
from src.models.prisms import Prism
from src.utils.configs.user_config import UserConfig


def build_avatar(config: UserConfig) -> Prism:
    return build_prism(config=config)

