from typing import Dict
from uuid import UUID, uuid4

from app.models.prisms import Prism
from app.models.vehicles import Vehicle


class Ship(Vehicle):
    id: UUID = uuid4()
    crew: Dict[UUID, Prism]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


