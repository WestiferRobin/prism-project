from uuid import UUID, uuid4

from pydantic import BaseModel

from src.utils.constants import INITIAL_VERSION


class Config(BaseModel):
    version: int = INITIAL_VERSION
    id: UUID
    name: str
    alias: str

    def __init__(self,
        version: int,
        name: str,
        alias: str,
        config_id: UUID = None,
        **config_data
    ):
        if config_id is None:
            config_id = uuid4()
        super().__init__(
            version=version,
            id=config_id,
            name=name,
            alias=alias,
            **config_data
        )

