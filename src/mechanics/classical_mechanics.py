import numpy as np
from src.graph.model import Graph

class MotionSegment:
    """Represents a single segment of motion with acceleration, velocity, and position equations."""
    def __init__(self, acceleration, initial_velocity, initial_position, t_start):
        self.acceleration = acceleration
        self.initial_velocity = initial_velocity
        self.initial_position = initial_position
        self.t_start = t_start  # Start time of the motion segment

    def compute_velocity(self, t):
        """Computes velocity at time t, ensuring continuity."""
        return self.initial_velocity + self.acceleration(self.t_start) * (t - self.t_start)

    def compute_position(self, t):
        """Computes position at time t, ensuring continuity."""
        return (
            self.initial_position
            + self.initial_velocity * (t - self.t_start)
            + 0.5 * self.acceleration(self.t_start) * (t - self.t_start) ** 2
        )

class MotionSimulation:
    """Manages multiple motion segments and ensures smooth transitions."""
    def __init__(self):
        self.graph = Graph("Position-Time Graph", y_axis="Position(x)", x_axis="Time(t)")
        self.motion_segments = []
        self.time_stamps = [0]  # Initialize time tracking

    def add_motion(self, t_end, acceleration_function):
        """Adds a new motion segment and ensures continuity."""
        t_start = self.time_stamps[-1]  # Last known time

        if not self.motion_segments:
            initial_velocity, initial_position = 0, 0
        else:
            last_segment = self.motion_segments[-1]
            initial_velocity = last_segment.compute_velocity(t_start)
            initial_position = last_segment.compute_position(t_start)

        # Create a new motion segment
        new_segment = MotionSegment(acceleration_function, initial_velocity, initial_position, t_start)
        self.motion_segments.append(new_segment)
        self.time_stamps.append(t_end)

        # Generate time array for plotting
        times = np.linspace(t_start, t_end, 100)
        self.plot_motion(times, new_segment)

    def plot_motion(self, times, segment):
        """Plots position, velocity, and acceleration for a given segment."""
        self.graph.plot_function(
            lambda t: np.array([segment.compute_position(ti) for ti in t]), times, "position(t)", "blue"
        )
        self.graph.plot_function(
            lambda t: np.array([segment.compute_velocity(ti) for ti in t]), times, "velocity(t)", "green"
        )
        self.graph.plot_function(
            lambda t: np.full_like(t, segment.acceleration(segment.t_start)), times, "acceleration(t)", "red"
        )

    def run_simulation(self):
        """Displays the final graph with all motion segments."""
        self.graph.plot()

# --- Running the Simulation ---
if __name__ == "__main__":

    """
    Notes:
    - Did a draft but had gpt polish for me since im new at this modeling thing
    - Goal is to make ai drones and star armada using drones for Trade and Battle Missions
    - FotF Inspires Dream:
        - I control a droid armada
        - I can do Trade and Battle missions
        - Will have all or none full star ships of drones
        - Will have shuttles, fighters, speeders, probes to help on star ships
        - All ships hail from colonies to do Trade and Battle missions
        
    - Newton
        
    """

    sim = MotionSimulation()

    sim.add_motion(1, lambda t: 1)

    sim.add_motion(2, lambda t: -2 * t)

    sim.run_simulation()
