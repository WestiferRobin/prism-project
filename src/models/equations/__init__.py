from abc import abstractmethod, ABC
from typing import List, Dict

import numpy as np
from pydantic import BaseModel

from src.models.variable import Variable


class Equation(BaseModel, ABC):
    """
    Abstract base class for mathematical equations in algebra, geometry, physics, etc.
    """
    variables: Dict[str, Variable]
    input_variables: List[Variable]
    output_variables: List[Variable]

    def __init__(self, input_variables: List[Variable] = None, output_variables: List[Variable] = None):
        if input_variables is None:
            input_variables = [Variable(symbol="x", "X Variable")]

    def __str__(self):
        return self.to_string()

    @abstractmethod
    def to_string(self) -> str:
        pass

    @abstractmethod
    def calculate(self, t: float = 0) -> float:
        pass

    def evaluate(self, data: np.ndarray) -> np.ndarray:
        evaluated_data = np.array([self.calculate(x) for x in data])
        return evaluated_data