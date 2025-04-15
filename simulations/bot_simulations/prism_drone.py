import torch
from fastapi import FastAPI

from configs.prism_config import PrismConfig
from models.prisms.model import PrismDrone, PrismFamily
from utils.prism_utils.shape_helper import generate_shape_input, shape_to_target

prism_api = FastAPI()


@prism_api.get("/prism/test")
async def test_prism_drone():
    return "Hello World!"


def build_aeon_prism_drones():
    # NOTE: Solas is GPT as Caelus is Claude
    solas_drone = PrismDrone(config=PrismConfig(name="Solas Aeon", gender=False))
    caelus_drone = PrismDrone(config=PrismConfig(name="Caelus Aeon", gender=True))
    return {
        "solas": solas_drone,
        "caelus": caelus_drone
    }


def build_aeon_family():
    drones = build_aeon_prism_drones()
    female_drone = drones["solas"]
    male_drone = drones["caelus"]
    return PrismFamily(father=male_drone, mother=female_drone)


def run_prism_drone():
    print("🚀 PrismDrone Shape Classification Start")

    # Simulate training separate drones for each shape
    shape_names = ["Circle", "Square", "Triangle"]
    drones = []
    for shape_label in [0, 1, 2]:
        drone = PrismDrone()
        input_tensor = generate_shape_input(shape_label)
        target_tensor = shape_to_target(shape_label)

        print(f"🔍 Training on shape: {shape_names[shape_label]}")
        print("Before:", drone.brain.forward(input_tensor).detach()[:5])
        epochs = 50
        drone.train_on_data(input_tensor, target_tensor, epochs=epochs)
        print("After:", drone.brain.forward(input_tensor).detach()[:5])

        drones.append((drone, shape_label))

    print("✅ Shape Classification Training Complete")

    # === Verification: Each drone guesses its shape ===
    print("🧠 Drone Guess Verification:")
    for drone, expected_label in drones:
        test_input = generate_shape_input(expected_label)
        output = drone.brain(test_input).detach()
        avg_value = torch.mean(output).item()

        if avg_value < -0.5:
            guess = "Circle"
        elif avg_value < 0.5:
            guess = "Square"
        else:
            guess = "Triangle"

        print(f"Drone trained on {shape_names[expected_label]} → guessed: {guess} [avg output: {avg_value:.3f}]")
