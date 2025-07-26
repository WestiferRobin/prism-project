from pydantic import BaseModel

from zlegacy.models import Model


class Sprite(BaseModel):
    sprite_model: Model

