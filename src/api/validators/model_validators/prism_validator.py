from uuid import UUID

from src.models.prisms import Prism
from src.utils.configs.model_configs.prism_config import PrismConfig


def validate_prism(prism: Prism) -> None:
    assert prism is not None
    assert isinstance(prism, Prism)

    assert prism.id is not None
    assert isinstance(prism.id, UUID)

    assert prism.name is not None
    assert isinstance(prism.name, str)

    assert prism.config is not None
    assert isinstance(prism.config, PrismConfig)

