from abc import abstractmethod
from uuid import UUID

from pydantic import BaseModel


class Model(BaseModel):
    id: UUID
    name: str

    @abstractmethod
    def update(self, command: Command = None):
        pass
