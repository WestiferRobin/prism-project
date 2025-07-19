from typing import List

import numpy as np

from src.models.equations import Equation
from src.models.graphs import Graph, GraphAxis
from src.models.variable import Variable


def build_graph_axis(symbol: str, label: str, data: np.array) -> GraphAxis:
    return GraphAxis(
        symbol=symbol,
        label=label,
        data=data,
    )

def build_variable_axis(variable: Variable, variable_data: np.array) -> GraphAxis:
    return build_graph_axis(
        symbol=variable.symbol,
        label=variable.label,
        data=variable_data
    )


def build_graph(
    title: str,
    axes: List[GraphAxis],
    series_label: str = None
) -> Graph:
    return Graph(
        title=title,
        axes={ axis.symbol: axis for axis in axes },
        series_label=series_label
    )

def build_2d_graph(title: str, x_axis: GraphAxis, y_axis: GraphAxis, series_label: str = None) -> Graph:
    return build_graph(
        title=title,
        axes=[x_axis, y_axis],
        series_label=series_label
    )


def build_equation_graph(equation: Equation) -> Graph:
    input_data = np.linspace(-10, 10)
    output_data = equation.evaluate(input_data)

    input_axis = build_variable_axis(variable=equation.input_variable, variable_data=input_data)
    output_axis = build_variable_axis(variable=equation.output_variable, variable_data=output_data)

    equation_title = f"{equation}"
    return build_2d_graph(
        title=equation_title,
        x_axis=input_axis,
        y_axis=output_axis,
        series_label=equation_title
    )