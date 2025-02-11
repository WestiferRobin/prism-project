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
    def __init__(self, version: int = 1):
        self.player_faction = AdminLegion()
        self.enemy_faction = AdminLegion()
        self.board = determine_board(version)
        # Needs to see planets like EAW: Corrupt Forces for Episodes 0-X (11 Episodes? Maybe 12?)
            # Idea: Player sees fleets per StarBase and can order them to attack or trade
        # Needs to battle like battlefront but it's a tactical shooter in rivals convoy
            # Idea: Battlefront Orbit Battles as Valorant Rivals game
        # Needs to land battle like AOE2 and Rimworld
            # Idea: Player builds base with drones in a AOE2 world
            # Workers gather resources for Base to build Farms, Mines, Lumberyard, Harbor, Houses
            # Tier 1 can build Troopers in Barracks
            # Tier 2 can build Tanks in Factory
            # Tier 3 can build Shuttles in Factory
            # Tier 4 can build Portals in StarBase
        # Needs to space battle like Battlefront and Rouge Squadron
            # Think Rivals logic between dogfight, support-ships, lead-ship of Fleet Battle
            # 1st Round fighter dogfight
            # 2nd Round defend support ships from fighters
            # 3rd Round defend lead ship from enemy fighters and support ships
                # Consider defend lead ship from enemy fighters and lead ships
            # Consider Orbit Battles between FleetShip and LegionBase
            # 1st Round secure area
            # 2nd Round secure wall
            # 3rd Round secure center
        # Needs to galactic conquest like Battlefront
            # Legion needs full armada with stockpile of resources
            # stockpiles stored on citadel bases connected at tier 4 level portals and ships
            # stockpiles stored on city bases with tier 3 ships
            # stockpiles stored on town bases with tier 2 ships
            # stockpiles stored on outpost bases with tier 1 ships
            # camp bases are created from tier 1 ships
        # Player needs to experience war in simulated battles in ranked-game, unrated-game, or quick-game
            # Game Modes:
                # Campaigns: Clone Wars, Civil Wars, Reminate Wars
                # Ranked => 1 v 1, 2 v 2, 4 v 4
                # Unrated => Ranked without score
            # Player's Avatar is Private to Admin or Baby to Elder
            # If dies goes to next avaliable heir otherwise loose
            # Starts on Battle Mission
            # Continue until Sergeant of Trade Mission
            # fails will become Ensign until Sergeant of Battle Mission
            # Sergeant does Trade and Battle Mission on Cruiser
            # Lieutenant does Science and Battle Mission on Cruiser
            # Lieutenant does Trade and Battle Mission on Frigate
            # Commander does Trade and Battle Mission on Frigate
            # Captain does Science and Battle Mission on Frigate
            # Captain does Trade and Battle Mission on Capital
            # Major does Trade and Battle Mission on Capital
            # Major is elected for being Arch Guardian
            # Arch Guardian is voted to AdminGeneral or AdminAdmiral
            # General or Admiral can be voted as ViceAdmin
            # ViceAdmin as Leader of LegionArmada
            # ArchAdmin as Leader of LegionOrder in Sol of Galaxy

def build_drone_squadron(leader: PrismDrone = None):
    if leader is None:
        leader = PrismDrone(rank=LegionRank.Sergeant)
    squadron = (
        leader,
        PrismDrone(rank=LegionRank.Lance),
        PrismDrone(rank=LegionRank.Corporal),
        PrismDrone(rank=LegionRank.Corporal),
        PrismDrone(rank=LegionRank.Private),
        PrismDrone(rank=LegionRank.Private),
        PrismDrone(rank=LegionRank.Private),
        PrismDrone(rank=LegionRank.Private)
    )
    return squadron

def build_fighter_squadron():
    leader = SpaceFighter(PrismDrone(rank=LegionRank.Lance))
    squadron = (
        leader,
        SpaceFighter(PrismDrone(rank=LegionRank.Lance)),
        SpaceFighter(PrismDrone(rank=LegionRank.Lance)),
        SpaceFighter(PrismDrone(rank=LegionRank.Corporal)),
        SpaceFighter(PrismDrone(rank=LegionRank.Corporal)),
        SpaceFighter(PrismDrone(rank=LegionRank.Corporal))
    )
    return squadron

def build_shuttle_squadron():
    squadron = build_drone_squadron()
    lead_pilot = squadron[1]
    co_pilot = squadron[2]
    crew = (
        squadron[0],
        squadron[3:]
    )
    return SpaceShuttle(lead_pilot, co_pilot, crew)

def build_star_cruiser():
    return StarCruiser()

def build_star_frigate():
    return StarFrigate()

def build_star_capital():
    return StarCapital()

def build_star_dreadnought():
    return StarDreadnought()

def build_star_fleet():
    star_cruiser = build_star_cruiser()
    star_frigate = build_star_frigate()
    star_capital = build_star_capital()
    fleet = (
        star_cruiser,
        star_frigate,
        star_capital,
    )
    return fleet

def build_star_armada():
    flagship = build_star_dreadnought()
    elite_fleet = (
        flagship,
        build_star_capital(),
        build_star_capital()
    )
    armada = (
        elite_fleet,
        build_star_fleet(),
        build_star_fleet()
    )
    return armada

if __name__ == "__main__":
    star_armada = build_star_armada()
    print(star_armada)



