from enum import Enum
from typing import List


class FactionType(str, Enum):
    Federation = "Federation"
    Empire = "Empire"
    Exchange = "Exchange"
    Confederacy = "Confederacy"
    Pirate = "Pirate"
    Raider = "Raider"
    Union = "Union"
    Guild = "Guild"

    @staticmethod
    def build_list() -> List["FactionType"]:
        faction_list = [faction for faction in FactionType]
        return faction_list

    @property
    def title(self) -> str:
        return {
            FactionType.Federation: "The Solar Federation",
            FactionType.Empire: "The Ethereal Empire",
            FactionType.Exchange: "The Imperial Exchange",
            FactionType.Confederacy: "The Sovereign Confederacy",
            FactionType.Pirate: "The Pirate Syndicate",
            FactionType.Raider: "The Raider Alliance",
            FactionType.Union: "The Droid Union",
            FactionType.Guild: "The Merchant's Guild",
        }.get(self, self.value)


class MagicType(int, Enum):
    NoMagic = 0 # Default

    # Grand Arts
    Light = 10
    Dark = -10

    # Advanced Arts
    Mind = 8
    Spirit = -8
    Water = 6
    Fire = -6

    # Standard Arts
    Air = 3
    Thunder = -3
    Grass = 2
    Rock = -2
