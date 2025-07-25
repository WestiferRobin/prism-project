from uuid import UUID

from pydantic import BaseModel


class Response(BaseModel):
    response_id: UUID

