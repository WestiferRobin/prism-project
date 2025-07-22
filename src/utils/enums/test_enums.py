from enum import Enum


class TestGrade(int, Enum):
    E = 100 # Legacy Ready
    A = 90 # Production Ready
    B = 80 # Demo Ready
    C = 70 # Feature Ready
    D = 60 # Test Ready
    F = 50 # Dev Ready

