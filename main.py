from src.api.builders.vehicle_builder import build_speeder
from src.api.runner import run_controlled_experiment


def main():
    orb_speeder = build_speeder()
    run_controlled_experiment(orb_speeder)


if __name__ == "__main__":
    main()
