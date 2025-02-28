from src.models.drones.prism import PrismDrone
from src.models.solars.galaxy import MilkywayGalaxy, UniverseGalaxy
from src.models.legions.legion import AdminLegion


def determine_board(version: int = 0):
    if version == 0:
        return UniverseGalaxy()
    elif version == 1:
        return MilkywayGalaxy()
    else:
        raise Exception(f"Cannot play game with known board version {version}")


class FotfGame:
    def __init__(self, avatar: PrismDrone, version: int = 0):
        self.player_avatar = avatar
        self.board = determine_board(version)

        self.player_faction = AdminLegion()
        self.raider_faction = ArchLegion()
        self.pirate_faction = ArchLegion()
        self.enemy_faction = AdminLegion()
        self.setup()

    def setup_player_faction(self):

    def setup(self):

        self.apply_faction(self.player_faction, self.board.first_quadrant)
        self.apply_faction()
        self.apply_faction(self.enemy_faction, self.board.fourth_quadrant)
        """
        Sol adds Admin, Vice, Admiral, General:
        - Inner Belt:
            - Mercury: Admin Legion Stations and Bases
            - Venus: Admiral on StarStation with Admiral StarShips
            - Earth: Admin on StarBase and Vice on LunaBase
            - Mars: General with 2 LunaBases with General StarTroopers and StarWorkers => StarAcademy
            - Asteroid Belt: Admin Legion Stations and Bases
        - Outer Belt
            - Jupiter: Admin LegionFleet Station and Bases
            - Saturn: Admin LegionFleet Station and Bases
            - Uranus: General LegionFleet Station and Bases
            - Neptune: Admiral LegionFleet Station and Bases
            - Pluto: Admin Legion Stations and Bases
            - Asteroid Belt: Admin Legion Stations and Bases
        """

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

