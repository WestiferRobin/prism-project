from abc import abstractmethod

from pydantic import BaseModel

from app.models.commands import Command


class Model(BaseModel):
    name: str

    @abstractmethod
    def update(self, command: Command = None):
        pass
