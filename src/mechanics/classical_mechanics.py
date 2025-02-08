import numpy as np

from src.graph.model import Graph

class PositionEquation:
    def __init__(self, acceleration, initial_velocity, initial_position):
        self.acceleration = acceleration
        self.velocity = lambda t: initial_velocity + t * self.acceleration(t)
        self.position = lambda t: initial_position + t * initial_velocity + 0.5 * self.acceleration(t) * t ** 2

class PositionGraph:
    def __init__(self, position_variable: str="x", time_variable: str="t"):
        self.graph = Graph("Position-Time Graph", y_axis=f"Position({position_variable})", x_axis=f"Time({time_variable})")

    def plot_interval(self, t_start, t_end, equation: PositionEquation):
        times = np.linspace(t_start, t_end)
        self.graph.plot_function(lambda t: equation.position(t), times, "position(t)", "blue")
        self.graph.plot_function(lambda t: equation.velocity(t), times, "velocity(t)", "green")
        self.graph.plot_function(lambda t: equation.acceleration(t), times, "acceleration(t)", "red")

    def plot_area(self, t_start, t_end, equation: PositionEquation):
        times = np.linspace(t_start, t_end)
        self.graph.plot_area(lambda t: equation.position(t), times, "position(t)", "blue")
        self.graph.plot_area(lambda t: equation.velocity(t - t_end + t_start), times, "velocity(t)", "green")
        self.graph.plot_area(lambda t: equation.acceleration(t - t_end + t_start), times, "acceleration(t)", "red")

    def show(self):
        self.graph.plot()


if __name__ == "__main__":
    graph = PositionGraph()

    asdf = PositionEquation(lambda t : t*0 + 1, 0, 0)
    graph.plot_interval(0, 1, asdf)

    fdsa = PositionEquation(lambda t : t*0 - 1, asdf.velocity(1), asdf.position(1))
    graph.plot_area(1, 2, fdsa)

    graph.show()
