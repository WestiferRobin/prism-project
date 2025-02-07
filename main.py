from src.models.vehicles.legion_armada import AdminLegion
from src.simulations.nexus_simulations import run_nexus_simulation


def run_model():
    legion = AdminLegion(username="Wes")
    print(legion)


def run_simulation():
    run_nexus_simulation()


if __name__ == "__main__":
    run_simulation()

    # Update both computers to latest python
    # Create a rest api in prism-agent-service using nexus_framework
    # Create a frontend app in prism-web-app using react with prism-agent-service locally

