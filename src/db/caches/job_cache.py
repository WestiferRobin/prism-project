from typing import List, Optional
from uuid import UUID

from src.db.caches import get_redis
from src.db import EXPIRED_ACCOUNT_SECONDS, EXPIRED_USER_SECONDS
from src.db import (
    build_user_jobs_key,
    build_job_key,
    build_account_jobs_key,
)
from zlegacy.app.schemas import JobSchema

class RedisJobCache:
    def __init__(self):
        self.redis = get_redis()

    async def save_job(self, job: JobSchema) -> None:
        job_key = build_job_key(job.id)
        user_key = build_user_jobs_key(job.user_id)
        account_key = build_account_jobs_key(job.account_id)

        job_json = job.model_dump_json()

        await self.redis.set(job_key, job_json, ex=EXPIRED_ACCOUNT_SECONDS)
        await self.redis.sadd(user_key, str(job.id))
        await self.redis.expire(user_key, EXPIRED_USER_SECONDS)
        await self.redis.sadd(account_key, str(job.id))

    async def save_account_jobs(self, account_id: UUID, jobs: List[JobSchema]) -> None:
        account_key = build_account_jobs_key(account_id)
        pipe = self.redis.pipeline()

        for job in jobs:
            key = build_job_key(job.id)

            job_json = job.model_dump_json()

            pipe.set(key, job_json, ex=EXPIRED_ACCOUNT_SECONDS)
            pipe.sadd(account_key, str(job.id))

        await pipe.execute()

    async def save_user_jobs(self, user_id: UUID, jobs: List[JobSchema]) -> None:
        user_key = build_user_jobs_key(user_id)
        pipe = self.redis.pipeline()

        for job in jobs:
            key = build_job_key(job.id)
            account_key = build_account_jobs_key(job.account_id)

            job_json = job.model_dump_json()

            pipe.set(key, job_json, ex=EXPIRED_ACCOUNT_SECONDS)
            pipe.sadd(user_key, str(job.id))
            pipe.sadd(account_key, str(job.id))

        pipe.expire(user_key, EXPIRED_USER_SECONDS)
        await pipe.execute()

    async def get_job(self, job_id: UUID) -> Optional[JobSchema]:
        job_key = build_job_key(job_id)

        result = await self.redis.get(job_key)
        if not result:
            return None

        return JobSchema.model_validate_json(result)

    async def get_account_jobs(self, account_id: UUID) -> List[JobSchema]:
        job_ids = await self.redis.smembers(build_account_jobs_key(account_id))
        jobs: List[JobSchema] = []

        for job_id in job_ids:
            try:
                job = await self.get_job(UUID(job_id))
                if job:
                    jobs.append(job)
            except ValueError:
                continue  # Skip bad UUIDs

        return jobs

    async def get_user_jobs(self, user_id: UUID) -> List[JobSchema]:
        job_ids = await self.redis.smembers(build_user_jobs_key(user_id))
        jobs: List[JobSchema] = []

        for job_id in job_ids:
            try:
                job = await self.get_job(UUID(job_id))
                if job:
                    jobs.append(job)
            except ValueError:
                continue

        return jobs

    async def invalidate_job(self, job_id: UUID) -> None:
        await self.redis.delete(build_job_key(job_id))

    async def invalidate_account_jobs(self, account_id: UUID) -> None:
        job_ids = await self.redis.smembers(build_account_jobs_key(account_id))
        for job_id in job_ids:
            await self.invalidate_job(UUID(job_id))

        await self.redis.delete(build_account_jobs_key(account_id))

    async def invalidate_user_jobs(self, user_id: UUID) -> None:
        job_ids = await self.redis.smembers(build_user_jobs_key(user_id))
        for job_id in job_ids:
            await self.invalidate_job(UUID(job_id))

        await self.redis.delete(build_user_jobs_key(user_id))
