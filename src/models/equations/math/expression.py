from pydantic import BaseModel


class Expression(BaseModel):
    value: str

