from src.models.equations import Equation
from sympy import Function as SymFunction


class Function(Equation, SymFunction):
    symbol: chr
    parameters: List[Variable]

    def __init__(self,
        symbol: chr,
        parameters: List[Variable],
        expression: Expression,
        *args,
        **options
    ):
        parameter_label = ""
        if len(parameters) == 0:
            raise PrismException(f"No parameters for this function {symbol}")
        else:
            for index in range(len(parameters) - 1):
                parameter_label += f"{parameters[index]}, "
            parameter_label += f"{parameters[len(parameters) - 1]}"

        super().__init__(
            name=f"{symbol}",
            symbol=chr,
            parameters=parameters,
            left_hand_side=Expression(value=f"{symbol}({parameter_label})"),
            right_hand_side=expression,
            args=args,
            options=options
        )

