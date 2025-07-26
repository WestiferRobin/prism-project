from pydantic import BaseModel

from src.utils.configs.bot_configs.server_config import ServerConfig


class HiveServer(BaseModel):
    config: ServerConfig

