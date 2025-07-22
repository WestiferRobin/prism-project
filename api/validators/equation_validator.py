from typing import Set, Dict, List

from app.models.equation import Equation


def validate_expression(expression: str):
    assert expression is not None
    assert type(expression) is str


def validate_arguments(
    arguments: Set[str],
    parameters: Set[str],
    input_variables: Set[str],
    output_variables: Set[str]
):
    for variable in input_variables:
        assert variable in arguments
    for variable in output_variables:
        assert variable not in arguments
    for parameter in parameters:
        assert parameter in arguments


def validate_parameters(parameters: Set[str], input_variables: Set[str], output_variables: Set[str]):
    for variable in input_variables:
        assert variable not in parameters

    for variable in output_variables:
        assert variable not in parameters


def validate_variables(variables: Set[str], input_variables: Set[str], output_variables: Set[str]):
    for variable in input_variables:
        assert variable in variables

    for variable in output_variables:
        assert variable in variables


def validate_equation_is_valid(equation: Equation, condition: Dict[str, float], expected_value: bool):
    valid_condition = condition.copy()
    if not expected_value:
        for variable in equation.input_variables:
            del valid_condition[variable]

    result = equation.is_valid(condition=valid_condition)
    assert type(result) is bool
    assert result == expected_value

def validate_equation_solve(equation: Equation, condition: Dict[str, float]):
    variable_conditions = condition.copy()
    for variable in equation.output_variables:
        del variable_conditions[variable]
    result = equation.solve(condition=variable_conditions)
    assert type(result) is Dict[str, float]
    assert result

def validate_equation_properties(equation: Equation):
    validate_expression(equation.expression)
    validate_arguments(equation.arguments, equation.parameters, equation.input_variables, equation.output_variables)
    validate_parameters(equation.parameters, equation.input_variables, equation.output_variables)
    validate_variables(equation.variables, equation.input_variables, equation.output_variables)

def validate_equation_condition(equation: Equation, condition: Dict[str, float]):
    validate_equation_is_valid(equation=equation, condition=condition, expected_value=True)
    validate_equation_is_valid(equation=equation, condition=condition, expected_value=False)
    validate_equation_solve(equation, condition)

def validate_equation(equation: Equation, conditions: List[Dict[str, float]]):
    assert equation is not None
    assert type(equation) is Equation

    validate_equation_properties(equation)
    for condition in conditions:
        validate_equation_condition(equation, condition)

