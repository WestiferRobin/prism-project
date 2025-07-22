import grpc

from db import settings
from messaging.rpc import media_job_pb2_grpc
from src.servers.job_server import MediaJobService
from src.utils.logger import get_logger

logger = get_logger(__name__)


async def serve() -> grpc.aio.Server:
    server = grpc.aio.server()
    media_job_pb2_grpc.add_MediaJobServiceServicer_to_server(MediaJobService(), server)
    server.add_insecure_port(f"[::]:{settings.grpc_content_port}")
    logger.info(f"[gRPC] prism-content-service gRPC Server running on port {settings.grpc_content_port}")
    await server.start()
    return server

