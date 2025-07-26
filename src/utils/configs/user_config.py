import uuid
from uuid import UUID

from src.utils.configs.prism_config import PrismConfig


class UserConfig(PrismConfig):
    user_id: UUID = uuid.uuid4()

    def __init__(self, user_id: UUID = None, **prism_data):
        if user_id is None:
            user_id = self.user_id
        super().__init__(user_id=user_id, dna=user_id, **prism_data)
