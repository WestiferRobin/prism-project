from enum import Enum


class GameMode(str, Enum):
    Skirmish = "skirmish" # 1v1 on 2x2 Galaxy Map of Stars
    Campaign = "campaign" # 1v3 on 3x3 Galaxy Map of Stars
    Classic = "classic" # 1v1 on 3x3 Galaxy Maps of Stars
    Royale = "royale" # 4v* on 2x2, 3x3, 4x4 Galaxy Maps of Stars


class GalaxyBoardType(int, Enum):
    Skirmish = 2
    Classic = 3
    Royale = 4

