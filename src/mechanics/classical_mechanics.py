import numpy as np

from src.graph.model import Graph, plot_function, plot_area


def acceleration(time):
    return time * 0 + 1


def velocity(time, initial_velocity):
    final_velocity = initial_velocity
    final_velocity += acceleration(time) * time
    return final_velocity


def position(time, initial_position, initial_velocity):
    final_position = initial_position
    final_position += initial_velocity * time
    final_position += (1/2) * acceleration(time) * time ** 2
    return final_position


if __name__ == "__main__":
    plot_graph = Graph("Physics", x_axis="t", y_axis="x")
    times = np.linspace(0, 1)
    position_0 = 0
    velocity_0 = 0
    plot_area(lambda t : position(t, position_0, velocity_0), times, "position(t)", "blue")
    plot_function(lambda t : velocity(t, velocity_0), times, "velocity(t)", "green")
    plot_function(lambda t : acceleration(t), times, "acceleration(t)", "red")
    plot_graph.plot()