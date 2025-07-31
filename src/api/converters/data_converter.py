from src.utils.exceptions import PrismException


def convert_nibble_to_hex(nibble: int) -> str:
    mapper = {digit: str(digit) for digit in range(0, 10)}
    mapper[10] = "A"
    mapper[11] = "B"
    mapper[12] = "C"
    mapper[13] = "D"
    mapper[14] = "E"
    mapper[15] = "F"

    if nibble not in mapper:
        raise PrismException(message=f"Invalid nibble value: {nibble}")

    return mapper[nibble]


def convert_byte_to_hex(value: int) -> str:
    if not (0 <= value <= 255):
        raise PrismException(message=f"Value must be a byte (0–255), got: {value}")

    high_nibble = (value & 0xF0) >> 4
    low_nibble = value & 0x0F

    high_hex = convert_nibble_to_hex(high_nibble)
    low_hex = convert_nibble_to_hex(low_nibble)

    hex_str = f"{high_hex}{low_hex}"
    return hex_str


