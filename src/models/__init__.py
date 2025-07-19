from abc import abstractmethod

from pydantic import BaseModel


class Model(BaseModel):
    name: str

    @abstractmethod
    def update(self):
        pass
