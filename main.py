from src.api.builders.vehicle_builder import build_speeder
from src.api.equations.force_equations.gravity_forces import GravityForce
from src.models.vehicles import Vehicle

"""

MISSION: Finish equation models

F(t) = m(t) * a(t), when a(t) = a + i*t
s(t) = s(0) + v(0) * t + (1/2) * a(t) * t^2
m(t) = density(t) * volume(t)

F = m(t) * integral(velocity(t))
"""
def validate_equations(vehicle: Vehicle):
    vehicle_mass = vehicle.mass
    print(vehicle_mass)  # "1 kg"

    gravity_force = GravityForce(vehicle_mass)
    gravity_force_unit = gravity_force
    print(f"F(t) = m(t) * g = {gravity_force_unit}")


    # TODO: Finish the following
    # print(f"W(t) = F(t) * Length(t) ")
    # density of said mass
    # look and do validation_test


def main():
    orb_speeder = build_speeder(1)
    validate_equations(orb_speeder)


if __name__ == "__main__":
    main()

