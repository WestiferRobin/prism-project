from zlegacy.api.handlers.si_helper import convert_kilo_to_cm3


def calculate_gram_mass(mass_density: float, mass_volume: float) -> float:
    # density is g/cm^3 and volume is in cm
    return mass_density * mass_volume

def calculate_mass(mass_density: float, mass_volume: float, is_kilo=True) -> float:
    if is_kilo:
        return mass_density * mass_volume
    gram_density = calculate_gram_mass(mass_density, mass_volume)
    return convert_kilo_to_cm3(gram_density, mass_density)

