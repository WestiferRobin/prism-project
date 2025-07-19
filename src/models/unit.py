from pydantic import BaseModel


class Unit(BaseModel):
    value: float
    unit: str

    def __str__(self):
        return f"<{self.value} {self.unit}>"

