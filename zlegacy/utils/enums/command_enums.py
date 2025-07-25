from enum import Enum


class CommandType(str, Enum):

    # ex.) Trooper and Ship Commands
    Confirm = 0
    Cancel = -1
    Attack = 1
    Defend = 2
    Interact = 3
    Inventory = 4
    Retreat = 5


class RequestType(int, Enum):
    Standard = 0


class ResponseType(int, Enum):
    Standard = 0

