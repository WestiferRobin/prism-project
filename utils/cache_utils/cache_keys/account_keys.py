from uuid import UUID


def build_account_key(account_id: UUID) -> str:
    return f"account:{account_id}"


def build_user_accounts_key(user_id: UUID) -> str:
    return f"user:{user_id}:accounts"

