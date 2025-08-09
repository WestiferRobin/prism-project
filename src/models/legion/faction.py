from typing import List, Dict
from uuid import UUID

from src.models.colonies.legion_colony import LegionColony
from src.models.drones.legion_drone import LegionDrone
from src.models.fleets.legion_fleet import LegionFleet
from src.models.legion import Legion
from src.utils.configs.model_configs.faction_config import FactionConfig



class Faction(Legion):
    colonies: List[LegionColony]
    armada: List[LegionFleet]

    # TODO: Need to figure out the colony vs leader_config issue for Faction
    def __init__(self,
        config: FactionConfig,
        colonies: List[LegionColony],
        armada: List[LegionFleet]
    ):
        super().__init__(
            config=config,
            colonies=colonies,
            armada=armada
        )

    @property
    def population(self) -> Dict[UUID, LegionDrone]:
        registry = {}

        for colony in self.colonies:
            for drone_id in colony.population:
                drone = colony.population[drone_id]
                registry[drone_id] = drone

        for fleet in self.armada:
            for drone_id in fleet.population:
                drone = fleet.population[drone_id]
                registry[drone_id] = drone

        return registry

    @property
    def admin(self) -> LegionDrone:
        return self.population[self.config.admin_config.id]

    @property
    def vice(self) -> LegionDrone:
        return self.population[self.config.vice_config.id]

    @property
    def general(self) -> LegionDrone:
        return self.population[self.config.general_config.id]

    @property
    def admiral(self) -> LegionDrone:
        return self.population[self.config.admiral_config.id]

    @property
    def leaders(self) -> Dict[UUID, LegionDrone]:
        registry = dict()
        if self.admin.is_alive():
            registry[self.admin.id] = self.admin
        if self.vice.is_alive():
            registry[self.vice.id] = self.vice
        if self.general.is_alive():
            registry[self.general.id] = self.general
        if self.admiral.is_alive():
            registry[self.admiral.id] = self.admiral
        return registry

