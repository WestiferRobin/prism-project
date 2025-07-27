from random import choice, randint

from src.utils.constants.name_constants import MALE_NAME_POOL, FEMALE_NAME_POOL
from src.utils.enums.color_enums import ColorType
from src.utils.enums.prism_enums import GenderType, RaceType


def create_robot_name() -> str:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter_part = "".join(choice(alphabet) for _ in range(2))
    number_part = f"{randint(0, 99):02d}"  # Ensures 2-digit number (e.g., 01, 42)
    return f"{letter_part}-{number_part}"


def create_last_name() -> str:
    last_names = [color.name for color in ColorType]
    return choice(last_names)


def create_male_name(race: RaceType) -> str:
    return choice(MALE_NAME_POOL[race])


def create_female_name(race: RaceType) -> str:
    return choice(FEMALE_NAME_POOL[race])


def create_first_name(gender: GenderType, race: RaceType) -> str:
    if gender == GenderType.Male:
        return create_male_name(race=race)
    elif gender == GenderType.Female:
        return create_female_name(race=race)
    else:
        return create_robot_name()


def create_name(gender: GenderType, race: RaceType) -> str:
    if race in [RaceType.Droid, RaceType.Android, RaceType.Cyborg]:
        return create_robot_name()
    else:
        last_name = create_last_name()
        first_name = create_first_name(gender, race)
        return f"{first_name} {last_name}"

