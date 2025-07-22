from enum import Enum
from random import choice

from src.utils.enums.faction_enums import FactionType
from src.utils.exceptions import NexusException




class RaceType(str, Enum):
    Human = "Human" # White, Brown, Black with Blue, Green, Blue and Red, Blonde, Brown, Black
    Aeon = "Aeon" # Vulkans / Snow Elves
    Archon = "Ethereal" # Sith / Blood Elves

    Slug = "Slug" # Hutts but Tank
    Bug = "Bug" # Rodians
    Reptile = "Reptile" # Reptilians, Abadoys, Trandosians

    Mammal = "Mammal" # Wookies, Klingon, Vikings
    Ape = "Ape" # Confederacy of the Apes
    Raptor = "Raptor" # Birds, Parrots, Crows, Ravens

    Shark = "Shark" # Atlantis and King Shark
    Fish = "Fish" # Mon Kalimari
    Squid = "Squid" # Dathomearians

    Droid = "Droid" # B1 Battle Droid / Protocol Droid
    Android = "Android" # Commander Data / Terminator / Greys
    Cyborg = "Cyborg" # Droid Union taking Organics into Cyborgs, Droids, and Androids


    @staticmethod
    def random_faction_race(faction: FactionType) -> "RaceType":
        race_list = []
        if faction == FactionType.Federation:
            race_list = [
                RaceType.Aeon,
                RaceType.Human,
                RaceType.Mammal,
                RaceType.Raptor,
                RaceType.Fish,
            ]
        elif faction == FactionType.Empire:
            race_list = [
                RaceType.Aeon,
                RaceType.Human,
                RaceType.Mammal,
                RaceType.Raptor,
                RaceType.Fish,
            ]
        elif faction == FactionType.Exchange:
            race_list = [
                RaceType.Slug
            ]
        elif faction ==
        else:
            return RaceType.Human

        return choice(race_list)




class AgeType(int, Enum):
    Baby = 0
    Child = 6
    Teen = 13
    Adult = 20
    Senior = 80
    Ancient = 120

    def __init__(self, age: int):
        self.age = age

    @staticmethod
    def find_type(age: int) -> "AgeType":
        if age < 0:
            raise NexusException("Age value cannot be negative")
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
    Male = "Male"
    Female = "Female"
    Unknown = "Unknown"


class RankType(str, Enum):
    # Worker Ranks
    Cadet = "Cadet" # Family's make Babies that become kids in academy, teens in university, adults in legion system
    Private = "Private" # Able to do Trade, Battle, and Stories for FactionLegion

    # Trooper Ranks
    Lance = "Lance" # Able to choose Primary Specialty
    Corporal = "Corporal" # Able to be drivers

    # Officer Ranks => Manager Ranks
    Ensign = "Ensign" # Able to be pilots
    Sergeant = "Sergeant" # Able to lead trooper or fighter squadron
    Lieutenant = "Lieutenant"

    # Gold Ranks
    Commander = "Commander" # Leader of Outpost and Cruiser
    Captain = "Captain" # Leader of Outpost and Frigate
    Major = "Major" # Leader of City and Capital
    Colonel = "Colonel"

    # Diamond Ranks
    Arch = "Arch"  # Arch is a General/Admiral with Atlantean or Etheral Magic
