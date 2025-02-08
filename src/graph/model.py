import matplotlib.pyplot as plt
import numpy as np
from sympy.physics.units import acceleration


def plot_function(function, inputs, label: str, color: str):
    outputs = function(inputs)
    plt.plot(inputs, outputs, label=label, color=color)


def plot_area(function, inputs, label: str, color: str, transparent: float = 0.3):
    plot_function(function, inputs, label, color)
    plt.fill_between(inputs, function(inputs), color=color, alpha=transparent)


class Graph:

    def __init__(self, title: str, x_axis: str = "X", y_axis: str = "Y"):
        self.title = title
        self.x_axis = x_axis
        self.y_axis = y_axis

    def plot(self):
        plt.axhline(0, color='black')
        plt.axvline(0, color='black')
        plt.xlabel(f"{self.x_axis} axis")
        plt.ylabel(f"{self.y_axis} axis")
        plt.legend()
        plt.title(self.title)
        plt.grid()
        plt.show()

def sample_graph():
    graph = Graph("sample graph")
    plot_function(lambda x : np.sin(x), np.linspace(0, 2 * np.pi), "sin(x)", "blue")
    plot_area(lambda  x : np.cos(x), np.linspace(0, 2 * np.pi), "cos(x)", "red")
    plot_area(lambda x : x / 3, np.linspace(0, np.pi), "y=mx+b", color="orange")
    plot_area(lambda x: -x / 3 + 2.1, np.linspace(np.pi, 2 * np.pi), "y=mx+b", color="green")
    graph.plot()

if __name__ == "__main__":
    sample_graph()