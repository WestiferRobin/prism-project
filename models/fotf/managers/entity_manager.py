
class EntityManager:
    def __init__(self):
        self.entities = {}

    def register(self, entity_id, data):
        self.entities[entity_id] = data

    def remove(self, entity_id):
        if entity_id in self.entities:
            del self.entities[entity_id]

    def get(self, entity_id):
        return self.entities.get(entity_id, None)

