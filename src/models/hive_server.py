from typing import Dict, List
from uuid import UUID

from pydantic import BaseModel

from src.models.drones import Drone
from src.utils.configs.bot_configs.server_config import ServerConfig
from src.utils.exceptions import PrismException
from src.utils.user import User


class HedronServer(BaseModel):
    config: ServerConfig
    registry: Dict[UUID, Drone]

    @property
    def id(self) -> UUID:
        return self.config.bot_id

    @property
    def owner(self) -> User:
        return self.config.owner

    @property
    def avatar(self) -> Drone:
        return Drone(config=self.config.avatar)

    @property
    def companion(self):
        return Drone(config=self.config.companion)

    @property
    def drones(self) -> List[Drone]:
        return list(self.registry.values())

    def find_drone(self, drone_id: UUID) -> Drone:
        if drone_id not in self.registry:
            raise PrismException(message=f"Drone {drone_id} not found for {self.config.name}")
        return self.registry[drone_id]

