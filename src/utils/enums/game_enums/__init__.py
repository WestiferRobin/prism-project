from enum import Enum


class GameMode(str, Enum):
    Classic = "classic" # 1v1 on 2x2
    Campaign = "campaign" # 1v3 on 3x3
    Royale = "royale" # 4v* on 3x3

