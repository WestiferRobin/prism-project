"""

Imagine an AI agent that helps you manifest your goals through the user's faith, knowledge, and wisdom as variable to goals.

The more you engage with it, the more you will experience it, the more you will appriciate it. This app must be addicting
Modern apps are destroying the minds. This app must be geuine of love and respect embedded to it's material.

"""
from models.prisms.model import PrismDrone

class User:
    def __str__(self):
        return self.name

    def __init__(self, name: str, username: str):
        self.name = name
        self.username = username

def run_prism_scribe():
    print("Prism Scribe. A platform to better yourself with an AI Agent called a Prism Drone.")
    user = User("Wes", "westifer_robin")
    drone = PrismDrone()
    print(user, drone)
