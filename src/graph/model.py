import math
from typing import Tuple

import numpy as np
import matplotlib.pyplot as plt

from src.utils.plot_utils import plot_position_time_graph

"""
Universal graphing class to plot any mathematical function.

Parameters:
- title: Title of the graph.
- xlabel: Label for the x-axis.
- ylabel: Label for the y-axis.
- figsize: Tuple defining figure size.
"""
class Graph:

    def __init__(self, n: int = 8, m: int = None):
        self.n = n
        if m is None:
            m = n
        self.m = m


    def plot_position_time_graph(
        self,
        lambda_function,
        time_tag: str = None,
        position_tag: str = None,
        title: str = "Relativistic Motion Near Light Speed",
        time_bound: Tuple[int] = (0, 1)
    ):
        if time_tag is None:
            time_tag = 't'
        if position_tag is None:
            position_tag = 'lambda'
        plot_position_time_graph(
            time_function=lambda_function,
            time_tag=f"Time ({time_tag})",
            position_tag=f"Position ({position_tag})",
            title=title
        )

    def plot_velocity_time_graph(self, mu_function):
        time_tag =

    def plot(self, function, x_range=(-10, 10), y_range=(-10, 10), num_points=100, **kwargs):
        """
        Plots the given function over the specified x range.

        Parameters:
        - func: Function to be plotted.
        - x_range: Tuple (min, max) defining x values.
        - num_points: Number of points to generate between x_range.
        - kwargs: Additional parameters to pass to func (e.g., parameters for equations).
        """
        x_values = np.linspace(x_range[0], x_range[1], num_points)
        y_values = function(x_values, **kwargs)

        # Create the plot
        plt.figure(figsize=self.size)
        plt.plot(x_values, y_values, label=f'{function.__name__}', color='blue', linewidth=2)

        # Labels and title
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.title(self.title)
        plt.legend()
        plt.grid(True)

        # Show the graph
        plt.show()

    def results(self):
        pass


if __name__ == "__main__":
    graph_2d = Graph(2)
    graph_3d = Graph(3)
    plot_energy_density(graph_2d)
    plot_3d_vector_field(graph_3d)

