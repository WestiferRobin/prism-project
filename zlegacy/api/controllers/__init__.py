from abc import ABC, abstractmethod

from pydantic import BaseModel

from zlegacy.app.models import Model
from zlegacy.app.models import Command


class Controller(BaseModel, ABC):
    model: Model

    @abstractmethod
    def read_request(self, command: Command) -> None:
        pass


    @abstractmethod
    def write_command(self) -> Command:
        pass

