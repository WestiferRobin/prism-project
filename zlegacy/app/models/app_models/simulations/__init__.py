from abc import ABC, abstractmethod

from pydantic import BaseModel

from zlegacy.app.models import Model
from zlegacy.app.models.app_models.commands.requests import Request


class Simulation(BaseModel, ABC):
    name: str
    model: Model

    def run(self):
        while self.is_running:
            self.update()
            command = self.read_command()
            self.model.update(command)

    @abstractmethod
    def read_request(self, request: Request) -> Request:
        pass

    @abstractmethod
    def update(self):
        pass




