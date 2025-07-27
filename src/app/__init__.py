from uuid import UUID

from pydantic import BaseModel

from src.utils.configs.app_configs import AppConfig


class App(BaseModel):
    config: AppConfig

    @property
    def id(self) -> UUID:
        return self.config.app_id

    @property
    def name(self) -> str:
        return self.config.name

