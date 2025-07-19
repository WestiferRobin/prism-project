from src.exceptions import EngineException
from src.models.vehicles import Vehicle
from src.simulations import Simulation


def build_controlled_simulation(version: int = 0) -> Simulation:
    if version != 0:
        raise EngineException(f"{version} is not supported for controlled simulations/experiments.")
    else:
        return Simulation(
            name="Classic Mechanics",
            description="Control experiments modeling on classical mechanics before modern mechanics is introduced mathematically."
        )


def run_controlled_experiment(vehicle: Vehicle, version: int = 0) -> None:
    controlled_experiment = build_controlled_simulation(version)
    controlled_experiment.add_vehicle(vehicle)
    controlled_experiment.run()
