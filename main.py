from src.api.builders.vehicle_builder import build_speeder
from src.api.simulators import simulate

"""
MISSION: Finish equation models

F(t) = m(t) * a(t), when a(t) = a + i*t
s(t) = s(0) + v(0) * t + (1/2) * a(t) * t^2
m(t) = density(t) * volume(t)

F = m(t) * integral(velocity(t))
"""


def main():
    orb_speeder = build_speeder(1)
    print(orb_speeder)
    # simulate(orb_speeder)

if __name__ == "__main__":
    main()
