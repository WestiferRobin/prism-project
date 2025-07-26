from enum import Enum

from src.utils.enums.color_enums import ColorType


# Note think of Clan as Core in the military population size
class ClanType(int, Enum):
    # Prisoners/Slaves/Contractors/Laborers
    Epsilon = -1
    Tau = -2

    # Elite Clans
    Omega = 0 # Clan of Light
    Mu = 1 # Clan of Dark

    # War Clans
    Lambda = 2 # Master of Lambda Arts of Thunder
    Alpha = 4 # Master of Alpha Arts of Fire
    Gamma = 6 # Master of Gamma Arts of Grass
    Beta = 8 # Master of Beta Arts of Water

    # Trade Clans
    Psi = 3 # Master of Psi Arts of Mind
    Theta = 5 # Master of Theta Arts of Rock
    Phi = 7 # Master of Phi Arts of Spirit
    Sigma = 9 # Master of Sigma Arts of Air

    @property
    def color(self) -> ColorType:
        return {
            ClanType.Omega: ColorType.White,
            ClanType.Lambda: ColorType.Yellow,
            ClanType.Alpha: ColorType.Red,
            ClanType.Gamma: ColorType.Green,
            ClanType.Beta: ColorType.Blue,

            ClanType.Mu: ColorType.Black,
            ClanType.Psi: ColorType.Purple,
            ClanType.Theta: ColorType.Grey,
            ClanType.Phi: ColorType.Magenta,
            ClanType.Epsilon: ColorType.White,

            ClanType.Sigma: ColorType.Pink,
            ClanType.Tau: ColorType.Black,
        }.get(self, self.value)
        # return {
        #     FactionType.Federation: "The Solar Federation",
        #     FactionType.Empire: "The Ethereal Empire",
        #     FactionType.Exchange: "The Imperial Exchange",
        #     FactionType.Confederacy: "The Sovereign Confederacy",
        #     FactionType.Pirate: "The Pirate Syndicate",
        #     FactionType.Raider: "The Raider Alliance",
        #     FactionType.Union: "The Droid Union",
        #     FactionType.Guild: "The Merchant's Guild",
        # }.get(self, self.percent_value)

