"""
- Legion:
  - Leader: Prism(rank=Rank.Admin, name="Wes Black", clan="omega")
  - Vice: Prism(rank=Rank.Arch, name="John Red", clan="alpha")
  - Admiral: Prism(rank=Rank.Arch, name="Mr Goose", clan="lambda")
  - General: Prism(rank=Rank.Arch, name="Mei Theta", clan="theta")
  - armada:
    - royal_armada: Armada
    - legion_armada: Armada
  - population:
    - citizens:
      - royals: List[Drone]
      - leaders: List[Drone]
      - officers: List[Drone]
      - workers: List[Drone]
    - families: List[Family]
    - colonies: List[Colony]
    - territories: List[Territory]
    - stations: List[Station]
- Faction: Legion
  - resources: List[Resource]
"""

from pydantic import BaseModel
from src.models.prisms import Prism


class Legion(BaseModel):
    admin: Prism # TODO: Change to LegionDrone

