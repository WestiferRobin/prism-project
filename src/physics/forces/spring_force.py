from src.physics.forces import Force


class SpringForce(Force):
    def __init__(self, mass: callable, k: float, displacement: list[callable]):
        """
        Hooke's Law: F = -k * x, where x is displacement (per dimension).
        Assumes `displacement` is a list of callables per dimension.
        """
        spring_accelerations = [lambda t, a=a: -k * a(t) for a in displacement]
        super().__init__(mass, spring_accelerations)