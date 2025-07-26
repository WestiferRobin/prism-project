from typing import Dict
from uuid import UUID, uuid4

from zlegacy.models.app_models.prisms import Prism
from zlegacy.models.app_models.vehicles import Vehicle


class Ship(Vehicle):
    id: UUID = uuid4()
    crew: Dict[UUID, Prism]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


