from matplotlib import pyplot as plt

from app.models.graph import Graph


def plot_graph(graph: Graph):
    plt.figure()
    plt.plot(graph.x_data, graph.y_data, label=graph.series_label or "")
    plt.xlabel(graph.x_label)
    plt.ylabel(graph.y_label)
    plt.title(graph.title)
    if graph.series_label:
        plt.legend()
    plt.grid(True)
    plt.show()


