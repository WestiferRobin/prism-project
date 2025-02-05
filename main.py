from src.models.drones.model import PrismAgent


def engine_simulation():
    nexus_engine = NexusEngine()
    run_engine_simulation(nexus_engine)
    run_orb_simulation(nexus_engine)
    run_prism_simulation(nexus_engine)


class LegionArmada:
    def __init__(self):
        self.active_fleets = []
        self.base_fleet = []

class PrismAvatar(PrismAgent):

class AdminLegion:
    def __init__(self, username: str, user_tag: str, user_id):
        self.leader = PrismAvatar(name=username, seed=user_id, )
        self.armada = LegionArmada()
        self.bases = {}


if __name__ == "__main__":
    # TODO: Finish this once you have data model working for simulations for analysis for nexus-theory
    # run_engine_simulation()

    # This is the idea how my LegionArmada would look like
