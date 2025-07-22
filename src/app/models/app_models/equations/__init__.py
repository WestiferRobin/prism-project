from typing import List

from pydantic import BaseModel
from sympy import Function as SymFunction

from zlegacy.app.models import Expression
from zlegacy.app.models import Variable
from src.utils.exceptions import NexusException

# TODO: Need to validate equation class....
"""
Design: 
    - y = m * x + b 
        - f(t) = m * x(t) + b
        - x(t) = t
    - d^2 = x^2 + y^2 
        - d(t) = abs(sqrt((x(t) - x(0))^2 + (y(t) - y(0))^2))
        - z(t) = d(t)
    - x(t) = x(0) + v(0) * t + (1/2) * a(t) * t^2

1.) We need nums as floats
2.) We need parameters and variables to variable function
3.) We don't need to balance everything....


Equation.expression is Expression (which takes the string and makes valid for equation)
this means that....

class Expression(BaseModel):
    raw_value: str
    value: Eq.... maybe

class Equation(BaseModel):
    expression: Expression
    # Then get's variables and stuff from expression....

AC:
    1. Save progress as "paused on equation work to implement expression first"
    2. Work on Expression like Equation tests in same level of order.
    3. We get unit tests for Expression and Equation. Then we integrate them both for cases.
        - neg-inf to pos-inf


"""


class Equation(BaseModel):
    left_hand_side: Expression
    right_hand_side: Expression


class Function(Equation, SymFunction):
    symbol: chr
    parameters: List[Variable]

    def __init__(self,
        symbol: chr,
        parameters: List[Variable],
        expression: Expression,
        *args,
        **options
    ):
        parameter_label = ""
        if len(parameters) == 0:
            raise NexusException(f"No parameters for this function {symbol}")
        else:
            for index in range(len(parameters) - 1):
                parameter_label += f"{parameters[index]}, "
            parameter_label += f"{parameters[len(parameters) - 1]}"

        super().__init__(
            name=f"{symbol}",
            symbol=chr,
            parameters=parameters,
            left_hand_side=Expression(value=f"{symbol}({parameter_label})"),
            right_hand_side=expression,
            args=args,
            options=options
        )

