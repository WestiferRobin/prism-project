from src.models.engines.nexus_engine import NexusEngine


class LightEngine(NexusEngine):
    def __init__(self, ship_id):
        super().__init__(ship_id)