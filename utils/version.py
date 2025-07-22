from pydantic import BaseModel


class Version(BaseModel):
    number: int

