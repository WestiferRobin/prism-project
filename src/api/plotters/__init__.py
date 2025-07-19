from matplotlib import pyplot as plt

from src.models.graphs import Graph


def plot_graph(graph: Graph, show: bool = True, save_path: str = None):
    """
    Plot a time-series Graph using matplotlib.

    Args:
        graph (Graph): The Graph data model.
        show (bool): Whether to display the plot in a window.
        save_path (str): If provided, will save the plot to this path.
    """

    plt.figure(figsize=(8, 5))
    plt.plot(graph.times(), graph.values(), marker='o', linestyle='-', label=graph.label)

    plt.title(graph.title_label)
    plt.xlabel(graph.x_label)
    plt.ylabel(graph.y_label)
    plt.grid(True)
    plt.legend()

    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
    if show:
        plt.show()

    plt.close()

