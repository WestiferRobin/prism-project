from enum import Enum


class GradeScore(str, Enum):
    A = "Excellent"
    B = "Standard"
    C = "Average"
    D = "Poor"
    F = "Horrible"

    def __init__(self, value: int):
        self.percent_value = value

    @property
    def percent(self) -> float:
        if self.percent_value >= 200:
            self.percent_value = 200
        elif self.percent_value <= -100:
            self.percent_value = -100
        return self.percent_value / 100

    def __str__(self) -> str:
        return self.value

