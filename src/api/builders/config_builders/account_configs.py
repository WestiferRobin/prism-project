from uuid import UUID

from src.utils.configs.model_configs.account_config import AccountConfig


def build_account_config(
    version: int,
    user_id: UUID,
    app_name: str,
    app_alias: str
) -> AccountConfig:
    return AccountConfig(
        version=version,
        user_id=user_id,
        app_name=app_name,
        app_alias=app_alias
    )
