from typing import Tuple, List

from src.models.drones.model import Prism, PrismDrone
from src.models.vehicles.model import NexusEngine
from src.utils.enums.prism_enums import LegionRank


class OrbDrone:
    def __init__(self, pilot: PrismDrone, engines: Tuple = None, position: Tuple = None):
        self.pilot = pilot

        if engines is None:
            engines = (NexusEngine(pilot.id),)
        self.engines = engines

        if position is None:
            position = (0, 0, 0, 0)
        self.position = position

class RangeWeapon:
    def __init__(self, rounds: int):
        self.rounds = rounds
        self.current_rounds = self.rounds
        
class LaserCannon(RangeWeapon):
    def __init__(self, rounds=4):
        super().__init__(rounds)

class IonCannon(LaserCannon):
    def __init__(self, rounds=3):
        super().__init__(rounds)
        
class PlasmaCannon(LaserCannon):
    def __init__(self, rounds=2):
        super().__init__(rounds)

class MissileLauncher(RangeWeapon):
    def __init__(self, rounds=3):
        super().__init__(rounds)
        
class BombLauncher(MissileLauncher):
    def __init__(self, rounds=2):
        super().__init__(rounds)
        
class PhotonLauncher(BombLauncher):
    def __init__(self, rounds=1):
        super().__init__(rounds)

class SpaceSpeeder(OrbDrone):
    def __init__(self, pilot: PrismDrone, right_cannon: LaserCannon = None, left_cannon: LaserCannon = None):
        super().__init__(
            pilot=pilot,
            engines=(
                NexusEngine(pilot.id),
                NexusEngine(pilot.id),
                NexusEngine(pilot.id),
                NexusEngine(pilot.id)
            )
        )
        self.hull = 100
        self.right_cannon = LaserCannon() if right_cannon is None else right_cannon
        self.left_cannon = LaserCannon() if left_cannon is None else left_cannon


class SpaceFighter(SpaceSpeeder):
    def __init__(self,
                 pilot: PrismDrone,
                 right_cannon: LaserCannon = None,
                 left_cannon: LaserCannon = None,
                 launcher: MissileLauncher = None
     ):
        super().__init__(pilot, right_cannon, left_cannon)
        self.armor = 50
        self.shields = 25

        if launcher is None:
            launcher = MissileLauncher()
        self.launcher = launcher

class SpaceInterceptor(SpaceFighter):
    def __init__(self, pilot: PrismDrone):
        super().__init__(pilot, PlasmaCannon(), PlasmaCannon(), MissileLauncher())
        self.shields += 25

class SpaceBomber(SpaceFighter):
    def __init__(self, pilot: PrismDrone, co_pilot: PrismDrone):
        super().__init__(pilot, IonCannon(), IonCannon(), BombLauncher())
        self.co_pilot = co_pilot
        self.shields += 25
        self.armor += 25


class SpaceShuttle(SpaceSpeeder):
    def __init__(self, pilot: PrismDrone, co_pilot: PrismDrone = None, crew = None):
        super().__init__(pilot=pilot, right_cannon=PlasmaCannon(), left_cannon=PlasmaCannon())
        self.armor = 75
        self.shields = 50
        
        if co_pilot is None:
            self.co_pilot = None
        self.co_pilot = co_pilot

        if crew is None:
            crew = tuple([self.pilot, self.co_pilot])
        else:
            shuttle_crew = [self.pilot, self.co_pilot]
            for member in crew:
                shuttle_crew.append(member)
            crew = tuple(shuttle_crew)
        self.crew = crew

def example_build_ship(
        ship_name: str="The Red Hawk",
        lead_rank: LegionRank=LegionRank.Captain,
        vice_rank: LegionRank=LegionRank.Commander,
        officer_rank: LegionRank=LegionRank.Lieutenant
):
    lead_officer = PrismDrone(rank=lead_rank)
    ship_layout = {
        "ship_type": f"StarCapital: {ship_name}",
        "layout": {
            "quarters": ["families"],
            "hall": ["crew members"],
            "hanger": ["battle_squadron", "trade_squadron", "scout_squadron"],
            "bridge": {
                "lead_officer": lead_officer, # I sit in lead of ship command as Avatar on decisions
                "vice_officer": PrismDrone(rank=LegionRank.Commander), # Sitting as second in command and lead of command
                "tactical_officer": PrismDrone(rank=LegionRank.Commander), # Sitting as lead of battle troopers
                "engineer_officer": PrismDrone(rank=LegionRank.Lieutenant), # Sitting as lead of engineer workers
                "medical_officer": PrismDrone(rank=LegionRank.Lieutenant), # Sitting as lead of medical workers
                "science_officer": PrismDrone(rank=LegionRank.Lieutenant) # Sitting as lead of science workers
            },
        },
        "battle_squadron": {
                "squad_leader": SpaceFighter(pilot=PrismDrone(rank=LegionRank.Lance)),
                "squad_interceptor": SpaceInterceptor(pilot=PrismDrone(rank=LegionRank.Corporal)),
                "squad_bomber": SpaceBomber(pilot=PrismDrone(rank=LegionRank.Corporal), co_pilot=PrismDrone(rank=LegionRank.Private)),
                "squad_fighter": SpaceFighter(pilot=PrismDrone(rank=LegionRank.Private))
            },
            "trade_squadron": {
                "shuttle_squadron": SpaceShuttle(
                    pilot=PrismDrone(rank=LegionRank.Sergeant),
                    co_pilot=PrismDrone(rank=LegionRank.Corporal),
                    crew=(
                        PrismDrone(rank=LegionRank.Lance),
                        PrismDrone(rank=LegionRank.Corporal),
                        PrismDrone(rank=LegionRank.Private),
                        PrismDrone(rank=LegionRank.Private)
                    )
                ),
                "guard_squadron": {
                    "squad_leader": SpaceFighter(pilot=PrismDrone(rank=LegionRank.Lance)),
                    "squad_interceptor": SpaceInterceptor(pilot=PrismDrone(rank=LegionRank.Corporal)),
                    "squad_bomber": SpaceBomber(pilot=PrismDrone(rank=LegionRank.Corporal), co_pilot=PrismDrone(rank=LegionRank.Private)),
                    "squad_fighter": SpaceFighter(pilot=PrismDrone(rank=LegionRank.Private))
                }
            },
            "scout_squadron": {
                "shuttle_squadron": SpaceShuttle(
                    pilot=PrismDrone(rank=LegionRank.Sergeant),
                    co_pilot=PrismDrone(rank=LegionRank.Corporal),
                    crew=(
                        PrismDrone(rank=LegionRank.Lance),
                        PrismDrone(rank=LegionRank.Corporal),
                        PrismDrone(rank=LegionRank.Private),
                        PrismDrone(rank=LegionRank.Private)
                    )
                ),
                "guard_squadron": {
                    "squad_leader": SpaceFighter(pilot=PrismDrone(rank=LegionRank.Lance)),
                    "squad_speeder_crew": {
                        1: SpaceSpeeder(pilot=PrismDrone(rank=LegionRank.Corporal)),
                        2: SpaceSpeeder(pilot=PrismDrone(rank=LegionRank.Corporal)),
                        3: SpaceSpeeder(pilot=PrismDrone(rank=LegionRank.Private)),
                        4: SpaceSpeeder(pilot=PrismDrone(rank=LegionRank.Private))
                    }
                }
            }
    }

if __name__ == "__main__":
    example_build_cruiser()