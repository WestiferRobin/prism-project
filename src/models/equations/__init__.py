from pydantic import BaseModel

from src.models.equations.math.expression import Expression


class Equation(BaseModel):
    left_hand_side: Expression
    right_hand_side: Expression

