from uuid import UUID

from pydantic import BaseModel


class App(BaseModel):
    id: UUID
    name: str
