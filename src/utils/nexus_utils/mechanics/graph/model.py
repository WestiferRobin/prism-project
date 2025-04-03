import matplotlib.pyplot as plt
import numpy as np


class Graph:

    def __init__(self, title: str, x_axis: str = "X", y_axis: str = "Y"):
        self.title = title
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.labels = set()

    def plot_function(self, function, inputs, label: str, color: str):
        outputs = function(inputs)
        if label in self.labels:
            plt.plot(inputs, outputs, color=color)
        else:
            plt.plot(inputs, outputs, label=label, color=color)
            self.labels.add(label)

    def plot_area(self, function, inputs, label: str, color: str, transparent: float = 0.3):
        self.plot_function(function, inputs, label, color)
        plt.fill_between(inputs, function(inputs), color=color, alpha=transparent)

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
    graph.plot_function(lambda x : np.sin(x), np.linspace(0, 2 * np.pi), "sin(x)", "blue")
    graph.plot_area(lambda  x : np.cos(x), np.linspace(0, 2 * np.pi), "cos(x)", "red")
    graph.plot_area(lambda x : x / 3, np.linspace(0, np.pi), "y=mx+b", color="orange")
    graph.plot_area(lambda x: -x / 3 + 2.1, np.linspace(np.pi, 2 * np.pi), "y=mx+b", color="green")
    graph.plot()
    # TODO Figure out 3d stuff and packaging graphs

if __name__ == "__main__":
    sample_graph()