from pydantic import BaseModel

from src.utils.configs.model_configs.account_config import AccountConfig


class Account(BaseModel):
    config: AccountConfig

