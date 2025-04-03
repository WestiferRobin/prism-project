
class OrbDrone:

    def __str__(self):
        return self.name

    def __init__(self, name: str):
        self.name = name

def run_orb_drone():
    drone = OrbDrone("Wes's speeder")
    print(f"Orb Drone: {drone}")
