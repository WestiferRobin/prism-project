from src.models.unit import Unit

CONVERSION_TABLE = {
    ("g", "kg"): lambda v: v / 1000,
    ("kg", "g"): lambda v: v * 1000,
    ("cm", "m"): lambda v: v / 100,
    ("m", "cm"): lambda v: v * 100,
    ("cm³", "m³"): lambda v: v * 1e-6,
    ("m³", "cm³"): lambda v: v / 1e-6,
    ("g/cm³", "kg/m³"): lambda v: v * 1000,
    ("kg/m³", "g/cm³"): lambda v: v / 1000,
    ("C", "K"): lambda v: v + 273.15,
    ("K", "C"): lambda v: v - 273.15,
}


def convert_unit(unit: Unit, target_unit: str) -> Unit:
    if unit.unit == target_unit:
        return unit

    key = (unit.unit, target_unit)
    if key not in CONVERSION_TABLE:
        raise ValueError(f"No conversion for {unit.unit} → {target_unit}")

    converter = CONVERSION_TABLE[key]
    new_value = converter(unit.value)
    return Unit(new_value, target_unit)

