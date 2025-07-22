from pydantic import BaseModel

from app.models import Model


class View(BaseModel):
    model: Model

