from enum import Enum


class Environment(str, Enum):
    Dev = "DEV"
    Test = "TEST"
    Prod = "PROD"


