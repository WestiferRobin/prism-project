import math
from typing import Tuple

import numpy as np
from matplotlib import pyplot as plt

from src.graph.model import Graph


def plot_graph(title: str, y_tag: str, x_tag: str, graph: Graph):
    plt.plot(graph.results())
    plt.xlabel(x_tag)
    plt.ylabel(y_tag)
    plt.title(title)
    plt.grid(True)
    plt.show()


# Graph API Functions
def plot_position_time_graph(
    time_function,
    time_tag: str,
    position_tag: str,
    title: str,
    graph_range: Tuple[int] = (0, 16)
):
    t = np.linspace(graph_range[0], graph_range[1])

    position_result = time_function(t)

    plt.plot(t, position_result)
    plt.xlabel(time_tag)
    plt.ylabel(position_tag)
    plt.title(title)
    plt.grid(True)
    plt.show()


def plot_velocity_time_graph(time_function, time_tag, velocity_tag, title_tag):
    inital_position = time_function(0)
    final_position = time_function(2 * math.pi)


def plot_energy_density(graph: Graph):
    if graph.size() != 2:
        raise Exception(f"{graph.n} is in the Wrong Dimension. Not the 3rd Dimension.")
    x_vals = np.linspace(-1, 1, 100)
    y_vals = np.linspace(-1, 1, 100)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = 1 / np.sqrt(X**2 + Y**2 + 1e-6)  # Simplified energy density model
    plt.contourf(X, Y, Z, cmap="inferno")
    plt.colorbar(label="Energy Density")
    plt.xlabel("x (arbitrary units)")
    plt.ylabel("y (arbitrary units)")
    plt.title("Energy Density Around Electron Center of Mass")
    plt.show()

def plot_3d_energy_density(graph: Graph):
    if graph.size() != 3:
        raise Exception(f"{graph.n} is in the Wrong Dimension. Not the 3rd Dimension.")


def plot_3d_vector_field():
    x, y, z = np.meshgrid(np.linspace(-1, 1, 10),
                          np.linspace(-1, 1, 10),
                          np.linspace(-1, 1, 10))
    E_x = -y / np.sqrt(x**2 + y**2 + z**2 + 1e-6)
    E_y = x / np.sqrt(x**2 + y**2 + z**2 + 1e-6)
    E_z = 0  # Simplified case with no Z component
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.quiver(x, y, z, E_x, E_y, E_z, length=0.1, normalize=True)
    plt.title("3D Vector Field: EM Field Around the Orb")
    plt.show()
