from pydantic import BaseModel


class Variable(BaseModel):
    symbol: str
    label: str
    value: float = None

