from enum import Enum


class GravityType(float, Enum):
    Newton = 9.8 # acceleration meters
    Einstein = 6.67 # * 10^-11 kg m s as acceleration meters

