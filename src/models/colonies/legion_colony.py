from typing import Dict, List
from uuid import UUID

from src.models.colonies import Colony
from src.models.drones.legion_drone import LegionDrone


class LegionColony(Colony):
    population: Dict[UUID, LegionDrone]
    leader_id: UUID

    @property
    def leader(self) -> LegionDrone:
        return self.population[self.leader_id]

