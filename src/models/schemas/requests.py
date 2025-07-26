from uuid import UUID

from pydantic import BaseModel


class Request(BaseModel):
    request_id: UUID

