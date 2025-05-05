import math

from src.physics.forces import Force
from src.physics.kinematics import KinematicMotion
from src.ui.plotter.force_plotter import plot_force_results
from src.ui.plotter.kinematics_plotter import plot_kinematic_results


def run_kinematic_simulation(i_time: float = 0, f_time: float = 1, step: float = 0.01):
    kinematic_cases = [
        {
            "label": "1D Constant Acceleration",
            "motion": KinematicMotion(
                position=[0],
                velocity=[0],
                acceleration=[1]  # constant
            )
        },
        {
            "label": "2D Mixed Acceleration",
            "motion": KinematicMotion(
                position=[0, 0],
                velocity=[0, 0],
                acceleration=[
                    lambda t: 1,       # constant
                    lambda t: 9.8 * t  # linear increase
                ]
            )
        },
        {
            "label": "3D Function-Based Acceleration",
            "motion": KinematicMotion(
                position=[0, 0, 0],
                velocity=[0, 0, 0],
                acceleration=[
                    lambda t: math.sin(t),  # oscillatory
                    lambda t: 9.8,          # constant
                    lambda t: t**2          # quadratic
                ]
            )
        }
    ]

    for case in kinematic_cases:
        print(f"\n--- Simulating {case['label']} ---")
        results = case["motion"].simulate(i_time, f_time, step)
        plot_kinematic_results(results, dim_label=case['label'])

def run_force_simulation():
    # Acceleration = Force / Mass = a_x(t), a_y(t)
    mass_func = lambda t: 1.0
    acceleration_x = lambda t: -math.sin(t)  # like a spring pull
    acceleration_y = lambda t: 9.8  # gravity

    # 3. Create the force object
    force = Force(
        mass=mass_func,
        acceleration=[acceleration_x, acceleration_y]
    )

    # 4. Convert those acceleration functions to feed into KinematicMotion
    #    (a = F/m is already true, so we reuse acceleration_x/y directly)

    motion = KinematicMotion(
        position=[0, 0],  # initial position (x, y)
        velocity=[0, 0],  # initial velocity
        acceleration=force.acceleration  # pass a list of callables
    )

    # 5. Simulate from t = 0 to t = 5
    motion_results = motion.simulate(0, 5, 0.1)
    force_results = force.simulate(0, 5, 0.1)
    plot_kinematic_results(motion_results, "Motion Results")
    plot_force_results(force_results, "Force Results")


def run_newtonian_mechanics():
    # run_kinematic_simulation()
    run_force_simulation()
