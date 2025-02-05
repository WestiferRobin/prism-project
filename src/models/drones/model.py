import uuid

from src.utils.prism_utils import build_prism_nexus


class PrismAtom:
    def __init__(self, seed):
        self.particles = seed


class PrismCell:
    def __init__(self, seed):
        self.dna = seed


class Prism:
    def __init__(self, dna_id):
        self.mass = build_prism_nexus(dna_id)

    def cells(self):
        return self.mass["cells"]


class PrismAgent:
    def __init__(self, sprite: str, prism: Prism = None):
        self.sprite = sprite
        self.brain = Prism(uuid.uuid4()) if prism is None else prism

        self.__apply_brain()

    def __apply_brain(self):
        mass = self.brain.mass()
        cells = mass["cells"]
        cells = self.brain.mass


class PrismAvatar(PrismAgent):
    def __init__(self, avatar_sprite: str, user_id=None):
        if user_id is None:
            user_id = uuid.uuid4()
        super().__init__(sprite=avatar_sprite, prism=Prism(dna_id=user_id))


class PrismDrone(PrismAgent):
    def __init__(self, dna_id):
        super().__init__(dna_id)

class AvatarDrone(PrismAvatar):
    def __init__(self, avatar_sprite: str, user_id=None):
        if user_id is None:
            user_id = uuid.uuid4()
        super().__init__(sprite=avatar_sprite, prism=Prism(dna_id=user_id))


class PrismTrooper(PrismDrone):
    def __init__(self, dna_id):
        super().__init__(dna_id)


class PrismWorker(PrismDrone):
    def __init__(self, dna_id):
        super().__init__(dna_id)

