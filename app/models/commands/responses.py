from pydantic import BaseModel

from utils.enums import ResponseType


class Response(BaseModel):
    type: ResponseType = ResponseType.Standard

