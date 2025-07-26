from src.app.drone import Drone


class PrismDrone(Drone):
    health: int
    armor: PrismArmor = None

    @property
    def shields(self) -> PrismShields:
        if self.armor:
            return self.armor.shields
        else:
            return None

