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

    def start(self):
        """
        Nexus Engine:
        - 1 Magnetic Field
        - 1 Charge Field
        - 1 Mass of Alloy of Iron, Aluminum, and Copper

        1 Nexus Engine:
        W(t) = mgh + (1/2)mv^2 = (1/2)kx^2 + (1/2)mv^2
        P(t) = W(t)/t
        g(u,v) <= (8pi/c^4)G(u,v)

        OrbDrone: 4 Nexus Engine Graphs
        OrbDrone as Mass in Vacuum of Space with Plasma Mass of Suns
        OrbDrone as Mass in Solid Space of Earth
        OrbDrone as Mass in Gas Pressure of Atmosphere
        OrbDrone as Mass in Liquid Pressure of Oceans

        Proves OrbDrone as an all-terrain vehicle on Earth.
        """
        print(f"Starting Nexus Engine {self.id}")
        # Initialize magnetic and charge fields
        self.magnetic_field = 5.0  # Tesla
        self.charge_field = 1e5  # Volts/meter
        self.velocity = 0  # Initial velocity
        self.height = 0.5  # Initial height (m)

    def run(self, time_step=0.05, duration=10):
        """Simulate the Nexus Engine running over time."""
        import numpy as np
        import matplotlib.pyplot as plt

        time = np.arange(0, duration, time_step)
        heights = []

        for t in time:
            force = self.magnetic_field * self.charge_field * self.unit_mass  # Example force calculation
            acceleration = force / self.unit_mass
            self.velocity += acceleration * time_step
            self.height += self.velocity * time_step
            heights.append(self.height)

        plt.plot(time, heights, label="Orb Drone Height")
        plt.xlabel("Time (s)")
        plt.ylabel("Height (m)")
        plt.title("Nexus Engine Lift Simulation")
        plt.legend()
        plt.grid(True)
        plt.show()

    def stop(self):
        """Stop the Nexus Engine."""
        print(f"Stopping Nexus Engine {self.id}")
        self.velocity = 0

# Example usage
if __name__ == "__main__":
    engine = NexusEngine(ship_id="NX-01")
    engine.start()
    engine.run(duration=5)
    engine.stop()
