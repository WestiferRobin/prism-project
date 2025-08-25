from enum import Enum
from random import choice, randint
from src.utils.exceptions import PrismException

class RaceType(str, Enum):
    Human = "human" # earth humans and star humans
    Cyborg = "cyborg" # humans with cyber parts

    Aeon = "aeon" # white and blue and yellow and green elves
    Archon = "archon" # black and grey and red and orange demons

    Slug = "slug" # Jabba as Tzar of Exchange while Zimo as Vice Tzar
    Bug = "bug" # Common of Confederacy and Exchange
    Reptile = "reptile" # Common of Ethereal and Exchange

    Deer = "Deer" # Common of Federation and Guild
    Wolf = "wolf" # Common of Raiders and Guild
    Lion = "lion" # Common of Pirates and Raiders
    Bear = "bear" # Common of Pirates and Raiders

    Raptor = "raptor" # Common of Pirates and Guild
    Parrot = "parrot" # Common of Raiders and Guild
    Bird = "bird" # Common of Pirates and Raiders

    Shark = "shark" # Common of Ethereal and Exchange
    Orca = "orca" # Common of Federation and Guild
    Squid = "squid" # Common of Pirates and Raiders
    Fish = "fish" # Common of Ethereal nd Federation

    Droid = "droid" # droid but machine like
    Android = "android" # droid but human like

    @staticmethod
    def random_race() -> "RaceType":
        races = [race for race in RaceType]
        return choice(races)


class AgeType(int, Enum):
    Baby = 0
    Child = 6
    Teen = 13
    Adult = 20
    Senior = 80
    Ancient = 120

    def __init__(self, age: int = None):
        if age is None:
            age = AgeType.Adult.value
        self.age = age

    @staticmethod
    def random_age(min_age: int = None, max_age: int = None) -> "AgeType":
        if min_age is None:
            min_age = AgeType.Baby.value
        if max_age is None:
            max_age = AgeType.Ancient.value
        age = randint(min_age, max_age)
        return AgeType.find_type(age=age)

    @staticmethod
    def find_type(age: int) -> "AgeType":
        if age < 0:
            raise PrismException(message="Age percent_value cannot be negative", code=500)
        elif AgeType.Baby.age <= age < AgeType.Child.age:
            return AgeType.Baby
        elif AgeType.Child.age <= age < AgeType.Teen.age:
            return AgeType.Child
        elif AgeType.Teen.age <= age < AgeType.Adult.age:
            return AgeType.Teen
        elif AgeType.Adult.age <= age < AgeType.Senior.age:
            return AgeType.Adult
        elif AgeType.Senior.age <= age < AgeType.Ancient.age:
            return AgeType.Senior
        else:
            return AgeType.Ancient


class GenderType(str, Enum):
    Male = "male"
    Female = "female"
    Unknown = "unknown"

    @staticmethod
    def random_gender() -> "GenderType":
        genders = [gender for gender in GenderType]
        return choice(genders)


class RankType(int, Enum):
    # Standard Worker/Trooper Ranks
    Private = 0 # Able to do Trade, Battle, and Stories for FactionLegion
    Lance = 1 # Able to choose Primary Specialty
    Corporal = 2 # Able to be drivers

    # Advanced Worker/Trooper Ranks
    Ensign = 3 # Able to choose Secondary Speciality
    Sergeant = 4 # Able to lead trooper or fighter squadron
    Lieutenant = 5 # Able to lead trooper or ship officer

    # Manager/Officer Ranks
    Commander = 6 # Leader of Outpost and Cruiser
    Captain = 7 # Leader of Outpost and Frigate
    Major = 8 # Leader of City and Capital
    Colonel = 9 # Leader of City and

    # Leader Ranks
    Arch = 10  # Arch is a General/Admiral with Atlantean or Ethereal Magic. Admin is an Arch for Legion

    @staticmethod
    def random_rank() -> "RankType":
        ranks = [rank for rank in RankType]
        return choice(ranks)

