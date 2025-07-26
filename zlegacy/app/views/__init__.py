from pydantic import BaseModel

from zlegacy.models import Model


class View(BaseModel):
    model: Model

