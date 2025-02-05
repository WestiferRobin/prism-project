from src.models.vehicles.parts.engines import NexusEngine

def run_pre_ignition(nexus_engine: NexusEngine):
    nexus_engine.start()
    print("pre_ignition: Inconclusive")

def run_engine(nexus_engine: NexusEngine):
    nexus_engine.run()
    print("ignition: Inconclusive")

def run_post_ignition(nexus_engine: NexusEngine):
    nexus_engine.stop()
    print("post_ignition: Inconclusive")

def run_engine_simulation(engine: NexusEngine):
    run_pre_ignition(engine)
    run_engine(engine)
    run_post_ignition(engine)
