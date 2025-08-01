from uuid import UUID

from src.utils.configs import Config


class AccountConfig(Config):
    def __init__(self,
        version: int,
        user_id: UUID,
        app_name: str,
        app_alias: str,
    ):
        super().__init__(
            version=version,
            config_id=user_id,
            name=app_name,
            alias=app_alias
        )

    @property
    def user_id(self) -> UUID:
        return self.id

