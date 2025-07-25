from pydantic import BaseModel

from src.models.equations import Equation


class Force(BaseModel):
    equation: Equation

    def __init__(self, **force_data):
        super().__init__(**force_data)

