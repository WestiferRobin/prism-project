from pydantic import BaseModel

from zlegacy.app.models import Model


class View(BaseModel):
    model: Model

