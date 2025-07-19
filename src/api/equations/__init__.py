from abc import abstractmethod, ABC

from pydantic import BaseModel


class Equation(BaseModel, ABC):
    @abstractmethod
    def calculate(self, time: float = 0) -> float:
        pass

