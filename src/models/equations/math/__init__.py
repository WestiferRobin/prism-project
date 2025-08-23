from pydantic import BaseModel


class Position(BaseModel):
    x: float = 0 # aether per time in Space(time) Field
    y: float = 0
    z: float = 0
    w: float = 0

