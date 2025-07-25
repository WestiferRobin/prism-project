from pydantic.v1 import BaseSettings, Field
from pathlib import Path
import os


env_path = Path(__file__).parent.parent / ".env"


def is_running_inside_docker() -> bool:
    return os.path.exists("/.dockerenv") or os.getenv("DOCKER_ENV") == "1"


class Settings(BaseSettings):
    # 🌐 App Config
    app_port: int = Field(..., env="APP_PORT")

    # Postgres
    db_host: str = Field(..., env="DB_HOST")
    db_port: int = Field(..., env="DB_PORT")
    db_user: str = Field(..., env="DB_USER")
    db_password: str = Field(..., env="DB_PASSWORD")
    db_name: str = Field(..., env="DB_NAME")
    db_driver: str = Field("asyncpg", env="DB_DRIVER")

    # Redis
    redis_host: str = Field(..., env="REDIS_HOST")
    redis_port: int = Field(..., env="REDIS_PORT")

    # 🐰 RabbitMQ
    queue_content_host: str = Field(..., env="QUEUE_CONTENT_HOST")
    queue_content_port: int = Field(..., env="QUEUE_CONTENT_PORT")
    queue_content_user: str = Field(..., env="QUEUE_CONTENT_USER")
    queue_content_password: str = Field(..., env="QUEUE_CONTENT_PASSWORD")

    # gRPC
    grpc_engine_host: str = Field(..., env="GRPC_ENGINE_HOST")
    grpc_engine_port: int = Field(..., env="GRPC_ENGINE_PORT")

    class Config:
        env_file = str(env_path)
        env_file_encoding = "utf-8"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # 🔄 Local override for dev
        if not is_running_inside_docker():
            self.db_host = "localhost"
            self.db_port = 5433

            self.redis_host = "localhost"
            self.redis_port = 6380

            self.queue_content_host = "localhost"
            self.queue_content_port = 5673

            self.grpc_engine_host = "localhost"

    @property
    def database_url(self) -> str:
        return f"postgresql+{self.db_driver}://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    @property
    def cache_url(self) -> str:
        return f"redis://{self.redis_host}:{self.redis_port}"

    @property
    def queue_content_url(self) -> str:
        return f"amqp://{self.queue_content_user}:{self.queue_content_password}@{self.queue_content_host}:{self.queue_content_port}/"

    @property
    def grpc_engine_url(self) -> str:
        return f"{self.grpc_engine_host}:{self.grpc_engine_port}"


settings = Settings()

