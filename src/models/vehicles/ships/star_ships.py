from typing import Tuple

from src.models.drones.model import PrismDrone
from src.models.vehicles.engines.light_engine import LightEngine
from src.models.vehicles.ships.space_ships import OrbProbe, SpaceFighter, SpaceShuttle, SpaceSpeeder
from src.utils.enums.prism_enums import LegionRank

"""

TODO: Implement the following idea

Ship:
- Bridge:
    - lead_officer for All Missions with Ship
    - vice_officer for All Missions with Ship Weapons, Shields, Medial, Engines under Life Support
    - tactical_officer for Battle Missions and Ship Weapons, Mess Hall, Ship Simulator
    - science_officer for Science Missions and Ship Shields, Ship Farms, Science Labs
    - medical_officer for All Missions and Ship Medical, Ship Quarters, Medical Labs
    - engineer_officer for Trade Missions and Ship Engines, Life Support, Engineer Labs 

Thus we get

- BridgeConfig:
    - lead_officer of ship bridge
    - vice_officer of ship systems
    - first_officer of tactical systems
    - second_officer of science systems
    - third_officer of medical systems
    - fourth_officer of engineering systems

- ShipLayout:
    - UpperDeck:
        - Bridge: of lead_officers
        - Meeting Room: War Room
    - MidUpperDeck:
        - Hanger: of space-speeders in space-squadrons
        - Weapons: of 2, 3, 4, or 8
    - MidDeck:
        - Ship Quarters: Officer's Quarters and Quarter Exam
        - Ship Lab: Medical, Engineer, and Science Officers and Lab Exams
        - Ship Mess Hall: Ship's kitchen
        - Ship Simulator: Tactical Officers and Tactical Exams
    - LowerDeck:
        - Ship Farm: Science Officers
        - Ship Shields: Science Officers
        - Ship Life Support: Engineer Officers
        - Ship Engines: Engineer Officers

"""
class StarShip:
    """
    BridgeConfig:
    - lead_officer of ship bridge
    - vice_officer of ship systems
    - first_officer of tactical systems
    - second_officer of science systems
    - third_officer of medical systems
    - fourth_officer of engineering systems
    """
    def __init__(
            self,
            lead_officer: PrismDrone,
            vice_officer: PrismDrone,
            tactical_officer: PrismDrone,
            science_officer: PrismDrone,
            engineer_officer: PrismDrone,
            medical_officer: PrismDrone
    ):
        self.id = lead_officer.id
        self.lead_officer = lead_officer
        self.vice_officer = vice_officer
        self.tactical_officer = tactical_officer
        self.science_officer = science_officer
        self.engineer_officer = engineer_officer
        self.medical_officer = medical_officer

        self.layout = {}

        bridge = {
            "lead_chair": self.lead_officer,
            "vice_chair": self.vice_officer,
            "tactical_chair": self.tactical_officer,
            "science_chair": self.science_officer,
            "engineer_chair": self.engineer_officer,
            "medical_chair": self.medical_officer,
        }
        self.layout[0] = bridge

        hanger = { leader.id: None for leader in self.leaders() }
        weapons = { "cannons": {}, "launchers": {} }
        self.layout[1] = {
            "hanger": hanger,
            "weapons": weapons
        }

        quarters = { leader.id: {} for leader in self.leaders() }
        lab = {
            "medical_labs": { medical_officer.id: { } },
            "science_labs": { science_officer.id: { } },
            "engineer_labs": { engineer_officer.id: { } },
            "tactical_labs": { tactical_officer.id: { } }
        }
        social_hall = {
            "kitchen": {},
            "hall": {},
            "bar": {}
        }
        simulator = { }
        self.layout[2] = {
            "quarters": quarters,
            "lab": lab,
            "hall": social_hall,
            "simulator": simulator
        }

        farm = {}
        shields = {}
        engines = {
            "core": (
                LightEngine(self.id),
                LightEngine(self.id),
                LightEngine(self.id),
                LightEngine(self.id)
            )
        }
        life_support = {}
        cargo = {}
        self.layout[3] = {
            "farm": farm,
            "shields": shields,
            "engines": engines,
            "life_support": life_support,
            "cargo": cargo
        }

    def leaders(self):
        return self.layout[0].values()

    def crew(self):
        return self.leaders()


class StarCruiser(StarShip): # Outposts, Camps
    def __init__(
            self,
            lead_officer: PrismDrone,
            vice_officer: PrismDrone,
            tactical_officer: PrismDrone,
            science_officer: PrismDrone,
            engineer_officer: PrismDrone,
            medical_officer: PrismDrone
    ):
        super().__init__(
            lead_officer,
            vice_officer,
            tactical_officer,
            science_officer,
            engineer_officer,
            medical_officer
        )


class StarFrigate(StarShip): # Town, Outposts
    def __init__(
            self,
            lead_officer: PrismDrone,
            vice_officer: PrismDrone,
            tactical_officer: PrismDrone,
            science_officer: PrismDrone,
            engineer_officer: PrismDrone,
            medical_officer: PrismDrone
    ):
        super().__init__(
            lead_officer,
            vice_officer,
            tactical_officer,
            science_officer,
            engineer_officer,
            medical_officer
        )


class StarCapital(StarShip): # City, Town
    def __init__(
            self,
            lead_officer: PrismDrone,
            vice_officer: PrismDrone,
            tactical_officer: PrismDrone,
            science_officer: PrismDrone,
            engineer_officer: PrismDrone,
            medical_officer: PrismDrone
    ):
        super().__init__(
            lead_officer,
            vice_officer,
            tactical_officer,
            science_officer,
            engineer_officer,
            medical_officer
        )


class StarDreadnought(StarShip): # Citadel
    def __init__(
            self,
            lead_officer: PrismDrone,
            vice_officer: PrismDrone,
            tactical_officer: PrismDrone,
            science_officer: PrismDrone,
            engineer_officer: PrismDrone,
            medical_officer: PrismDrone
    ):
        super().__init__(
            lead_officer,
            vice_officer,
            tactical_officer,
            science_officer,
            engineer_officer,
            medical_officer
        )

