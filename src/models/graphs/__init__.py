from abc import ABC

from pydantic import BaseModel


class Graph(BaseModel, ABC):
    title: str

