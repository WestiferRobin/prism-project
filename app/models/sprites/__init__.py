from pydantic import BaseModel

from app.models import Model


class Sprite(BaseModel):
    sprite_model: Model

