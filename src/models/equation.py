from pydantic import BaseModel


class Equation(BaseModel):
    expression: str

    def __init__(self, **equation_data):
        super().__init__(**equation_data)

    def __str__(self):
        return self.expression
