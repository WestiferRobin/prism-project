import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn

from db import settings

# from messaging.queue_bindings import start_message_consumers
# from app.servers import serve

# from app.routes import service_router
# from app.routes.media_route import media_router

from db.database import init_db
# from utils import get_logger


logger = get_logger(__name__)

# TODO: Finish after unit tests are completed
@asynccontextmanager
async def lifespan(target_app: FastAPI):
    # Create DB tables
    await init_db()
    logger.info("[DB] Tables initialized")

    logger.info("[LIFESPAN] Starting prism-content-service...")

    grpc_server = await serve()  # Await queues serve, which starts and returns the server
    grpc_task = asyncio.create_task(grpc_server.wait_for_termination())

    # Start RabbitMQ consumers in background
    consumer_task = asyncio.create_task(start_message_consumers())

    yield  # App is running

    logger.info("[LIFESPAN] Shutting down prism-content-service...")
    consumer_task.cancel()  # Optional: cancel background tasks gracefully

    logger.info("[gRPC] Shutting down gRPC server...")
    await grpc_server.stop(grace=5)
    grpc_task.cancel()

app = FastAPI(
    title="Lab Engine Service",
    openapi_url="/api/v1/openapi.json",
    # lifespan=lifespan, TODO: Look at lifespan TODO
)

app.include_router(service_router)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=settings.app_port,
        log_level="debug",
        reload=False  # Turn on during dev only
    )

