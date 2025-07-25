from uuid import UUID

import grpc

from messaging.rpc import media_job_pb2, media_job_pb2_grpc

from src.services.mood_engine_service import update_job_status
from src.utils.logger import get_logger

logger = get_logger(__name__)


class MediaJobService(media_job_pb2_grpc.MediaJobServiceServicer):
    async def UpdateMediaJob(self,
        request: media_job_pb2.MediaJobRequest,
        context: grpc.aio.ServicerContext
    ) -> media_job_pb2.MediaJobResponse:
        try:
            logger.info(f"[gRPC] Received prism request: {request}")
            # TODO: Update the MediaModel with file_path either S3 or local

            response = update_job_status(
                owner_id=UUID(request.owner_id),
                prism_id=UUID(request.prism_id),
                job_id=UUID(request.job_id),
                job_status=request.status,
            )

            return media_job_pb2.MediaJobResponse(
                accepted=response.accepted,
                message=f"prism-content-service has verified for account_id='{request.owner_id}'"
            )
        except Exception as e:
            return media_job_pb2.MediaJobResponse(
                accepted=False,
                message=f"prism-content-service failed with exception: {e}"
            )

