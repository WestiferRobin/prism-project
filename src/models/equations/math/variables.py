from typing import List, Any

from pydantic import BaseModel
from sympy import Symbol


class Variable(Symbol):
    symbol: chr

    def __init__(self, symbol: str, **variable_assumptions: Any):
        super().__init__(
            symbol=symbol,
            name=symbol,
            assumptions=variable_assumptions
        )

class FunctionVariable(Variable):
    parameters: List[Variable]


class Point(BaseModel):
    parameters: List[Variable]


class Vector(Variable):
    source: Point



