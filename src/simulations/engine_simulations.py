import uuid

from src.models.vehicles.engines.nexus_engine import NexusEngine


def run_pre_ignition(engine: NexusEngine):
    engine.start()
    print("pre_ignition: Inconclusive")


def run_engine(engine: NexusEngine):
    engine.run(show_plot=False)
    print("ignition: Inconclusive")


def run_post_ignition(engine: NexusEngine):
    engine.stop()
    print("post_ignition: Inconclusive")


def run_engine_simulation(engine: NexusEngine):
    run_pre_ignition(engine)
    run_engine(engine)
    run_post_ignition(engine)


if __name__ == "__main__":
    nexus_engine = NexusEngine(
        ship_id=uuid.uuid4(),
        unit_mass=1,
        alloy_mass = {
            "Iron": 1,
            "Aluminum": 0,
            "Copper": 0
        }
    )
    run_engine_simulation(nexus_engine)
    # TODO: Need to start LightEngine() next after this is refactored!
