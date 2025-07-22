from abc import ABC, abstractmethod

from pydantic import BaseModel

from src.app.models.app_models.commands.requests import Request
from src.app.models.app_models.commands.responses import Response


class Command(BaseModel, ABC):
    name: str
    description: str

    @abstractmethod
    def execute(self, request: Request) -> None | Response:
        pass
