from typing import Dict, Set
from pydantic import BaseModel
from sympy import Eq, Symbol, lambdify
from sympy.parsing.sympy_parser import parse_expr
from sympy.core.function import AppliedUndef

# TODO: Need to validate equation class....
"""
Design: 
    - y = m * x + b 
        - f(t) = m * x(t) + b
        - x(t) = t
    - d^2 = x^2 + y^2 
        - d(t) = abs(sqrt((x(t) - x(0))^2 + (y(t) - y(0))^2))
        - z(t) = d(t)
    - x(t) = x(0) + v(0) * t + (1/2) * a(t) * t^2

1.) We need nums as floats
2.) We need parameters and variables to variable function
3.) We don't need to balance everything....


Equation.expression is Expression (which takes the string and makes valid for equation)
this means that....

class Expression(BaseModel):
    raw_value: str
    value: Eq.... maybe

class Equation(BaseModel):
    expression: Expression
    # Then get's variables and stuff from expression....
    
AC:
    1. Save progress as "paused on equation work to implement expression first"
    2. Work on Expression like Equation tests in same level of order.
    3. We get unit tests for Expression and Equation. Then we integrate them both for cases.
        - neg-inf to pos-inf


"""
class Equation(BaseModel):
    expression: str

    left_hand_side: Symbol = None
    right_hand_side: Symbol = None
    sym_equation: Eq = None

    arguments: Set[str] = set()
    input_variables: Set[str] = set()
    output_variables: Set[str] = set()
    parameters: Set[str] = set()
    variables: Set[str] = set()

    def __init__(self, **equation_data):
        if "=" not in self.expression:
            raise ValueError("Expression must contain an equals sign '='")

        lhs_str, rhs_str = map(str.strip, self.expression.split("=", 1))
        lhs_expr = parse_expr(lhs_str, evaluate=False)
        rhs_expr = parse_expr(rhs_str, evaluate=False)

        if isinstance(lhs_expr, AppliedUndef):
            lhs_expr = Symbol(str(lhs_expr.func))  # y(x) → y

        sym_eq = Eq(lhs_expr, rhs_expr)

        lhs_symbols = lhs_expr.free_symbols if isinstance(lhs_expr, Symbol) else set()
        rhs_symbols = rhs_expr.free_symbols

        arguments = {str(s) for s in lhs_symbols.union(rhs_symbols)}
        output_variables = {str(lhs_expr)} if isinstance(lhs_expr, Symbol) else set()
        input_variables = {str(s) for s in rhs_symbols.union(lhs_symbols) if str(s) not in output_variables}
        parameters = arguments - input_variables
        variables = {str(s) for s in sym_eq.free_symbols}
        super().__init__(**equation_data)

    def is_valid(self, condition: Dict[str, float]) -> bool:
        return self.input_variables.issubset(condition.keys())

    def solve(self, condition: Dict[str, float]) -> Dict[str, float]:
        if not self.is_valid(condition):
            missing = self.input_variables - set(condition.keys())
            raise ValueError(f"Missing input values for: {missing}")

        try:
            args = list(self.arguments)
            lhs_func = lambdify(args, self.left_hand_side, modules=["math"])
            rhs_func = lambdify(args, self.right_hand_side, modules=["math"])

            eval_args = {k: v for k, v in condition.items() if k in self.arguments}
            lhs_val = lhs_func(**eval_args)
            rhs_val = rhs_func(**eval_args)

            return {
                "lhs": lhs_val,
                "rhs": rhs_val,
                "valid": abs(lhs_val - rhs_val) < 1e-6
            }
        except Exception as e:
            raise ValueError(f"Evaluation failed: {e}")
