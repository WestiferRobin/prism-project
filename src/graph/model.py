import math

import numpy as np
import matplotlib.pyplot as plt

"""
Universal graphing class to plot any mathematical function.

Parameters:
- title: Title of the graph.
- xlabel: Label for the x-axis.
- ylabel: Label for the y-axis.
- figsize: Tuple defining figure size.
"""
class Graph:
    def __init__(self, title="Function Graph", x_label="X-axis", y_label="Y-axis", size=(8, 5)):
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.size = size

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

def x(t):
    return t

def y(t):
    return t

def f(t):
    x_initial = x(0)
    x_final = x(t * 2 * math.pi)
    y_initial = y(0)
    y_final = y(t * 2 * math.pi)

def f(x):
    pass

# Example usage
if __name__ == "__main__":
    graph = Graph(title="Test Graph")

    # Plot a quadratic function
    graph.plot(x, x_range=(-10, 10))

    # Plot a linear function
    graph.plot(y, x_range=(-10, 10))

    # # Plot a cubic function
    # graph.plot(cubic, x_range=(-10, 10), a=1, b=-2, c=1, d=0)

