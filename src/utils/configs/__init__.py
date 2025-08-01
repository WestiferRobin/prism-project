from uuid import UUID, uuid4

from pydantic import BaseModel

from src.utils.constants import DEV_VERSION


class Config(BaseModel):
    version: int
    id: UUID
    name: str
    alias: str

    def __init__(self, config_id: UUID = None, **config_data):
        if config_id is None:
            config_id = uuid4()
        super().__init__(
            id=config_id,
            **config_data
        )

