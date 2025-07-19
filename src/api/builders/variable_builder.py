from src.models.variable import Variable


def build_variable(symbol: str, label: str, value: float = None) -> Variable:
    return Variable(symbol=symbol, label=label, value=value)


def build_input_variable(symbol: str, label: str) -> Variable:
    return Variable(symbol=symbol, label=label)


def build_output_variable(symbol: str, label: str, value: float) -> Variable:
    return Variable(symbol=symbol, label=label, value=value)

