from src.models.vehicles.legion_armada import AdminLegion
from src.simulations.nexus_simulations import run_nexus_simulations
from src.simulations.ship_simulations import run_orb_simulations


def run_simulation():
    # run_nexus_simulations()
    run_orb_simulations()
    legion = AdminLegion(username="Wes")
    print(legion)


if __name__ == "__main__":
    run_simulation()

    # Update both computers to latest python
    # Create a rest api in prism-agent-service using nexus_framework
    # Create a frontend app in prism-web-app using react with prism-agent-service locally

