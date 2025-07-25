from enum import Enum


class UserTier(int, Enum):
    Basic = 0
    Standard = 1
    Advanced = 2
    Premium = 3
    
