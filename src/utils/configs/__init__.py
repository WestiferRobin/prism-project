from uuid import UUID, uuid4

from pydantic import BaseModel

from src.utils.constants import CURRENT_VERSION


class Config(BaseModel):
    version: int = CURRENT_VERSION
    id: UUID
    name: str
    alias: str = None

    def __init__(self,
        version: int,
        name: str,
        alias: str = None,
        config_id: UUID = None,
        **config_data
    ):
        if alias is None:
            alias = name.lower().replace(" ", "-")
        if config_id is None:
            config_id = uuid4()
        super().__init__(
            version=version,
            name=name,
            alias=alias,
            id=config_id,
            **config_data
        )

