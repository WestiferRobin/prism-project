from src.models.drones.model import PrismAgent, PrismAvatar


def nexus_simulation(engine: NexusEngine):
    run_engine_simulation(engine)
    run_orb_simulation(engine)
    run_prism_simulation(engine)

def engine_simulation(nexus_engine: NexusEngine):
    nexus_engine = NexusEngine()
    nexus_simulation(engine=NexusEngine())


class LegionArmada:
    def __init__(self):
        self.active_fleets = []
        self.base_fleet = []

class AdminLegion:
    def __init__(self, username: str, user_tag: str, user_id):
        self.leader = PrismAvatar(name=username, seed=user_id, )
        self.armada = LegionArmada()
        self.bases = {}


if __name__ == "__main__":
    # TODO: STOP EVERYTHING AND START nexus_mechanics.py
    """
    TODO: Need to learn this too
    Library	Purpose	Key Features
    NumPy (numpy)	General numerical operations arrays, vectors, matrix multiplications
    SymPy (sympy)	Symbolic tensor calculus differentiation, integrals, tensor algebra
    SciPy (scipy)	Solving tensor-based physics problems ODE&PDE solvers, numerical integration?
    PyTorch (torch)	High-performance tensor computations Automatic differentiation, optimized matrix operations
    
    build prism cell in 16x16x16 Volume
    build prism 16x16x16 Volume of cells
    build prism-drone as game-agent for fotf-simulations 
    """
    # run_engine_simulation()
    # Update both computers to latest python
    # Create a rest api in prism-agent-service using nexus_framework
    # Create a frontend app in prism-web-app using react with prism-agent-service locally

    # This is the idea how my LegionArmada would look like
