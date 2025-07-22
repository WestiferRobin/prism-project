from abc import ABC, abstractmethod

from pydantic import BaseModel

from app.models import Model
from app.models.commands import Command


class Controller(BaseModel, ABC):
    model: Model

    @abstractmethod
    def read_request(self, command: Command) -> None:
        pass


    @abstractmethod
    def write_command(self) -> Command:
        pass

