from uuid import UUID

from pydantic import BaseModel


class Sprite(BaseModel):
    model_id: UUID

