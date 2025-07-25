from uuid import UUID


def build_job_key(job_id: UUID) -> str:
    return f"job:{job_id}"


def build_account_jobs_key(account_id: UUID) -> str:
    return f"account:{account_id}:jobs"


def build_user_jobs_key(user_id: UUID) -> str:
    return f"user:{user_id}:jobs"

