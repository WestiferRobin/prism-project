
class KinematicMotionException(Exception):
    def __init__(self, position: list[float], velocity: list[float]):
        super().__init__(f"position({position}) and velocity({velocity}) dimensions don't match.")
