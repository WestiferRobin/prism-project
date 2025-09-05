from typing import List
from uuid import UUID

from src.api.builders.config_builders.account_configs import build_account_config
from src.models.accounts import Account


def build_account(
    version: int,
    app_name: str,
    app_alias: str,
    user_id: UUID
) -> Account:
    account_config = build_account_config(
        version=version,
        user_id=user_id,
        app_name=app_name,
        app_alias=app_alias,
    )
    return Account(config=account_config)


def build_accounts(
    version: int,
    app_name: str,
    app_alias: str,
    user_ids: List[UUID]
) -> List[Account]:
    accounts = []
    for user_id in user_ids:
        account = build_account(
            version=version,
            app_name=app_name,
            app_alias=app_alias,
            user_id=user_id,
        )
        accounts.append(account)
    return accounts

