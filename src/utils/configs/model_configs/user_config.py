import uuid
from uuid import UUID

from src.utils.configs.model_configs.prism_config import PrismConfig


class UserConfig(PrismConfig):
    user_id: UUID

    def __init__(self, user_id: UUID, **prism_data):
        super().__init__(user_id=user_id, dna=user_id, **prism_data)
