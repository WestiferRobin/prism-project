from src.api.builders.graph_builder import build_equation_graph
from src.api.plotters.graph_plotter import plot_graph
from src.models.equations.force_equations.gravity_forces import GravityForce
from src.models.vehicles import Vehicle


def simulate(vehicle: Vehicle):
    gravity_force = GravityForce(vehicle.mass)

    graph = build_equation_graph(gravity_force)
    plot_graph(graph)

