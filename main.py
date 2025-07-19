from src.api.builders.graph_builder import build_graph, build_equation_graph
from src.api.builders.vehicle_builder import build_speeder
from src.api.plotters.graph_plotter import plot_graph
from src.models.equations.force_equations.gravity_forces import GravityForce
from src.models.graphs import Graph
from src.models.vehicles import Vehicle

"""
MISSION: Finish equation models

F(t) = m(t) * a(t), when a(t) = a + i*t
s(t) = s(0) + v(0) * t + (1/2) * a(t) * t^2
m(t) = density(t) * volume(t)

F = m(t) * integral(velocity(t))
"""

def simulate(vehicle: Vehicle) -> Graph:
    gravity_force = GravityForce(vehicle.mass)
    return build_equation_graph(gravity_force)


def main():
    orb_speeder = build_speeder(1)

    force_graph = simulate(orb_speeder)
    plot_graph(force_graph)


if __name__ == "__main__":
    main()
