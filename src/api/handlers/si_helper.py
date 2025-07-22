def convert_kilo_to_cm3(kilo_mass: float, density_g_per_cm3: float) -> float:
    """
    Convert mass in kilograms to volume in cm³ using density in g/cm³.
    1 kg = 1000 g

    V = m / ρ
    """
    grams = kilo_mass * 1000
    return grams / density_g_per_cm3  # returns cm³


def convert_cm3_to_kilo(volume_cm3: float, density_g_per_cm3: float) -> float:
    """
    Convert volume in cm³ to mass in kg using density in g/cm³.
    m = ρ * V
    """
    grams = density_g_per_cm3 * volume_cm3  # mass in g
    return grams / 1000  # convert to kg
