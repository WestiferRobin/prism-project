from pydantic import BaseModel

from src.utils.configs.app_configs import TerminalConfig


class Terminal(BaseModel):
    config: TerminalConfig

