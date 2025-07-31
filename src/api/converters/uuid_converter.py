from uuid import UUID, uuid4

from src.api.converters.data_converter import convert_byte_to_hex


def convert_uuid_to_hex(value: UUID) -> str:
    hex_str = ""
    size = len(value.bytes)
    index = 0
    for byte in value.bytes:
        hex_str += convert_byte_to_hex(value=byte)
        index += 1
        if index % 4 == 0 and index < size - 1:
            hex_str += "-"
    return f"0x{hex_str}"


def convert_uuid_to_frequency(value: UUID) -> float:
    size = len(value.bytes)
    total = 0
    for byte in value.bytes:
        frequency = byte / 0xFF
        if 0.0 <= frequency < 0.25:
            total -= 2
        elif 0.25 <= frequency < 0.5:
            total -= 1
        elif 0.5 <= frequency < 0.75:
            total += 1
        elif 0.75 <= frequency < 1:
            total += 2
    return float(total / size)


def convert_uuid_to_int(value: UUID) -> int:
    frequency = convert_uuid_to_frequency(value=value)
    total = 0
    for byte in value.bytes:
        total += byte
    return int(total * frequency)

