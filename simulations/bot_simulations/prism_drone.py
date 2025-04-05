from fastapi import FastAPI

from models.prisms.model import PrismDrone

prism_api = FastAPI()

@prism_api.get("/prism/test")
async def test_prism_drone():
    return "Hello World!"

def run_prism_drone():
    drone = PrismDrone()
    print(f"Prism Drone: {drone}")
