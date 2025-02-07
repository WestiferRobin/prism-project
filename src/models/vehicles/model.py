
class NexusEngine:
    def __init__(self, ship_id):
        self.id = ship_id

    def start(self):
        pass

    def run(self):
        pass

    def stop(self):
        pass


class LightEngine(NexusEngine):
    def __init__(self, ship_id):
        super().__init__(ship_id)
