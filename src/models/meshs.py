from typing import List

from pydantic import BaseModel

from src.configs.vehicle_config import VehicleConfig


class Mesh(BaseModel):
    vertices: List[List[float]] = []
    faces: List[List[int]] = []


class VehicleMesh(Mesh):
    def __init__(self, config: VehicleConfig) -> None:
        super().__init__(config=config, vertices=[], faces=[])

