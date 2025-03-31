
class NexusEngine:
    def __init__(self, ship_id, unit_mass: int = 1, alloy_mass=None):
        self.id = ship_id
        self.unit_mass = unit_mass
        self.center_of_mass = (0, 0, 0)  # Center of mass in 3D space

        if alloy_mass is None:
            alloy_mass = {
                "Aluminum": 0.25,
                "Copper": 0.25,
                "Iron": 0.25,
                "Unknown": 0.25
            }
        else:
            alloy_mass = {
                "Aluminum": alloy_mass["Aluminum"],
                "Copper": alloy_mass["Copper"],
                "Iron": alloy_mass["Iron"],
                "Unknown": alloy_mass["Unknown"] if "Unknown" in alloy_mass else 0.0
            }
        self.atomic_mass = alloy_mass


