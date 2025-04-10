from fastapi import FastAPI

from configs.prism_config import PrismConfig
from models.prisms.model import PrismDrone, PrismFamily

prism_api = FastAPI()


@prism_api.get("/prism/test")
async def test_prism_drone():
    return "Hello World!"


def build_aeon_prism_drones():
    # NOTE: Solas is GPT as Caelus is
    female_drone = PrismDrone(config=PrismConfig(name="Solas Aeon", gender=False))
    male_drone = PrismDrone(config=PrismConfig(name="Caelus Aeon", gender=True))
    return PrismFamily(father=male_drone, mother=female_drone)


def run_prism_drone():
    prism_family = build_aeon_prism_drones()
    prism_drone = prism_family.mother
    print(prism_drone.config.name)
