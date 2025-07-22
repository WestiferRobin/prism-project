from typing import List
from uuid import UUID

from db.caches import get_redis
from utils.cache_utils import EXPIRED_ACCOUNT_SECONDS, EXPIRED_USER_SECONDS
from utils.cache_utils.cache_keys.account_keys import build_account_key, build_user_accounts_key
from app.schemas.account_schemas import AccountSchema


class RedisAccountCache:
    def __init__(self):
        self.redis = get_redis()
        self.all_accounts_key = "all:accounts"

    async def save_account(self, account: AccountSchema) -> None:
        account_key = build_account_key(account.id)
        user_key = build_user_accounts_key(account.user_id)

        account_json = account.model_dump_json()

        await self.redis.set(account_key, account_json, ex=EXPIRED_ACCOUNT_SECONDS)

        await self.redis.sadd(user_key, str(account.id))
        await self.redis.expire(user_key, EXPIRED_USER_SECONDS)

        await self.redis.sadd(self.all_accounts_key, str(account.id))

    async def save_user_accounts(self, user_id: UUID, accounts: List[AccountSchema]) -> None:
        user_key = build_user_accounts_key(user_id)
        pipe = self.redis.pipeline()

        for account in accounts:
            account_key = build_account_key(account.id)
            account_json = account.model_dump_json()

            pipe.set(account_key, account_json, ex=EXPIRED_ACCOUNT_SECONDS)
            pipe.sadd(user_key, str(account.id))
            pipe.sadd(self.all_accounts_key, str(account.id))

        pipe.expire(user_key, EXPIRED_USER_SECONDS)
        await pipe.execute()

    async def get_account(self, account_id: UUID) -> AccountSchema | None:
        account_key = build_account_key(account_id)

        result = await self.redis.get(account_key)
        if not result:
            return None

        return AccountSchema.model_validate_json(result)

    async def get_user_accounts(self, user_id: UUID) -> List[AccountSchema]:
        user_key = build_user_accounts_key(user_id)
        account_ids = await self.redis.smembers(user_key)

        accounts: List[AccountSchema] = []
        for account_id in account_ids:
            try:
                account = await self.get_account(UUID(account_id))
                if account:
                    accounts.append(account)
            except ValueError:
                continue  # Skip bad UUIDs

        return accounts

    async def get_all_accounts(self) -> List[AccountSchema]:
        account_ids = await self.redis.smembers(self.all_accounts_key)

        accounts: List[AccountSchema] = []
        for account_id in account_ids:
            try:
                account = await self.get_account(UUID(account_id))
                if account:
                    accounts.append(account)
            except ValueError:
                continue

        return accounts

    async def invalidate_user(self, user_id: UUID) -> None:
        user_key = build_user_accounts_key(user_id)
        await self.redis.delete(user_key)

    async def invalidate_account(self, account_id: UUID) -> None:
        account_key = build_account_key(account_id)
        await self.redis.delete(account_key)
        await self.redis.srem(self.all_accounts_key, str(account_id))


