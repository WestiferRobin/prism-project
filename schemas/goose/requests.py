from pydantic import BaseModel


class GooseRequest(BaseModel):
    strategy_name: str
    budget: float
