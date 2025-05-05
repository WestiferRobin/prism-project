from src.utils.exceptions.physics_exceptions.dimension_exceptions import KinematicMotionException

class KinematicMotion:
    def __init__(self, position: list[float], velocity: list[float], acceleration=None):
        if len(position) != len(velocity):
            raise KinematicMotionException(position, velocity)

        self.i_position = position
        self.i_velocity = velocity
        self.dim = len(self.i_position)

        # Handle default constant acceleration of 1.0 in all dimensions
        if acceleration is None:
            self.acceleration = [lambda t: 0.0 for _ in range(self.dim)]
        else:
            if len(acceleration) != self.dim:
                raise KinematicMotionException(position, velocity)  # Can make a better error here
            # Wrap constants as constant-returning functions
            self.acceleration = [
                (a if callable(a) else (lambda val=a: lambda t: val)()) for a in acceleration
            ]

    def position(self, time: float) -> list[float]:
        return [
            p + v * time + 0.5 * a(time) * time**2
            for p, v, a in zip(self.i_position, self.i_velocity, self.acceleration)
        ]

    def velocity(self, time: float) -> list[float]:
        return [
            v + a(time) * time
            for v, a in zip(self.i_velocity, self.acceleration)
        ]

    def simulate(self, i_time: float, f_time: float, step: float = 0.01) -> dict:
        intervals = {}
        time = i_time
        while time <= f_time:
            intervals[time] = {
                'position': self.position(time),
                'velocity': self.velocity(time),
                'acceleration': [a(time) for a in self.acceleration]
            }
            time += step
        return intervals
