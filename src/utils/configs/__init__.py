from pydantic import BaseModel


class Config(BaseModel):
    version: int = 0
    name: str
    alias: str = None

    def __init__(self,
        version: int,
        name: str,
        alias: str = None,
        **config_data
    ):
        if alias is None:
            alias = name.lower().replace(" ", "-")
        super().__init__(
            version=version,
            name=name,
            alias=alias,
            **config_data
        )

