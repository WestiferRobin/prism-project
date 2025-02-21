from src.models.drones.model import PrismDrone
from src.models.legion import AdminLegion
from src.models.planets.model import Sol
from src.models.vehicles.ships.space_ships import SpaceFighter, SpaceShuttle
from src.models.vehicles.ships.star_ships import StarCruiser, StarFrigate, StarCapital, StarDreadnought
from src.utils.enums.prism_enums import LegionRank


def determine_board(version: int):
    if version == 1:
        return Sol()
    else:
        raise Exception(f"Cannot play game with known board version {version}")


class FotfGame:
    def __init__(self, avatar: PrismDrone, version: int = 1):
        self.player_avatar = avatar
        self.player_faction = AdminLegion()
        self.enemy_faction = AdminLegion()
        self.board = determine_board(version)

    def is_running(self):
        if not self.player_avatar.is_alive():
            return False
        player_admin = self.player_faction.admin()
        enemy_admin = self.enemy_faction.admin()
        if player_admin.is_alive() and enemy_admin.is_alive():
            return True
        else:
            return False

    def winner(self):
        if self.is_running():
            return None
        player_admin = self.player_faction.admin()
        enemy_admin = self.enemy_faction.admin()
        if player_admin.is_alive() and not enemy_admin.is_alive():
            return player_admin
        elif not player_admin.is_alive() and enemy_admin.is_alive():
            return enemy_admin
        else:
            return None

    def loser(self):
        winner = self.winner()
        player_admin = self.player_faction.admin()
        enemy_admin = self.enemy_faction.admin()
        if winner is None:
            return None
        elif player_admin.id == winner.id:
            return enemy_admin
        elif enemy_admin.id == winner.id:
            return player_admin
        else:
            return None

    def is_tie(self):
        winner = self.winner()
        looser = self.loser()
        if winner is None and looser is None:
            return True
        else:
            return False


    def start(self):
        while self.is_running():
            self.update()
            break
        if self.is_tie():
            print("It's a draw")
        else:
            print(f"{self.winner()} wins in Solar Conquest")
            print(f"{self.loser()} looses in Solar Conquest")

    def update(self):
        pass


if __name__ == "__main__":
    game = FotfGame(PrismDrone(name="Wes"))

