import uuid

from src.models.drones.model import Prism
from src.models.vehicles.legion_armada import AdminLegion
from src.simulations.nexus_simulations import run_nexus_simulations
from src.simulations.prism_simulations import run_prism_simulations
from src.simulations.ship_simulations import run_orb_simulations


def run_test_simulations():
    run_nexus_simulations()
    run_prism_simulations(Prism(dna_id=uuid.uuid4()))
    run_orb_simulations()
    legion = AdminLegion(username="Wes")
    print(f"{legion} is ready for Valorant, Rivals, FTL, Battlefront Fotf Simulation?")


def run_debug_simulations():
    run_nexus_simulations()
    # run_prism_simulations(Prism(dna_id=uuid.uuid4()))
    # run_orb_simulations()


def run_simulation(is_debug: bool):
    if is_debug:
        run_debug_simulations()
    else:
        run_test_simulations()


if __name__ == "__main__":
    run_simulation(is_debug=True)

    # Update both computers to latest python
    # Create a rest api in prism-agent-service using nexus_framework
    # Create a frontend app in prism-web-app using react with prism-agent-service locally

