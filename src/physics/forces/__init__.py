"""
Forces and Newton’s Laws (F = m(t) * [a_x(t), a_y(t)])
"""

class Force:
    def __init__(self, mass: callable, acceleration: list[callable]):
        self.mass = mass
        self.acceleration = acceleration
        self.dim = len(self.acceleration)

    def force_vector(self, time: float = 0) -> list[float]:
        vector = []
        for a in self.acceleration:
            m_val = self.mass(time)
            a_val = a(time)
            vector.append(m_val * a_val)
        return vector

    def net_force(self, time: float = 0) -> float:
        f_vector = self.force_vector(time)
        return sum(f ** 2 for f in f_vector) ** 0.5

    def simulate(self, i_time: float, f_time: float, step: float = 0.01) -> dict[float, dict]:
        intervals = {}
        time = i_time
        while time <= f_time:
            time_rounded = round(time, 4)
            m_val = self.mass(time)
            a_vals = [a(time) for a in self.acceleration]
            f_vals = self.force_vector(time)

            intervals[time_rounded] = {
                'mass': m_val,
                'acceleration': a_vals,
                'vector': f_vals,
                'net': self.net_force(time)
            }
            time += step
        return intervals

