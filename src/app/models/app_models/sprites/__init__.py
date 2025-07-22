from pydantic import BaseModel

from zlegacy.app.models import Model


class Sprite(BaseModel):
    sprite_model: Model

