from utils.enums.solar_enums import SunColor


def find_terrestrial_count(sun_color: SunColor):
    if sun_color == SunColor.Yellow:
        return 4
    elif sun_color == SunColor.Orange:
        return 4
    elif sun_color == SunColor.Red:
        return 3
    elif sun_color == SunColor.Blue:
        return 2
    return 0

def find_jovian_count(sun_color: SunColor):
    if sun_color == SunColor.Yellow:
        return 4
    elif sun_color == SunColor.Orange:
        return 3
    elif sun_color == SunColor.Red:
        return 2
    elif sun_color == SunColor.Blue:
        return 4
    return 0

def find_dwarf_count(sun_color: SunColor):
    if sun_color == SunColor.Yellow:
        return 1
    elif sun_color == SunColor.Orange:
        return 0
    elif sun_color == SunColor.Red:
        return 0
    elif sun_color == SunColor.Blue:
        return 2
    return 0