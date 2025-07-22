from pydantic import BaseModel

from src.utils.enums import ResponseType


class Response(BaseModel):
    type: ResponseType = ResponseType.Standard

