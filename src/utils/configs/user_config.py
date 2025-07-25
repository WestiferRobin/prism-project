import uuid
from uuid import UUID

from src.utils.configs import Config


class UserConfig(Config):
    user_id: UUID = uuid.uuid4()


