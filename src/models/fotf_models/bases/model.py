import uuid


class LegionBase:
    def __init__(self, name: str, base_id=None):
        if base_id is None:
            base_id = uuid.uuid4()
        self.name = name
        self.id = base_id
