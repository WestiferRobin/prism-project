from src.models.drones.prism import PrismDrone
from src.models.engines.light_engine import LightEngine

"""

TODO: Implement the following idea

LegionShip:
- Bridge:
    - lead_officer for All Missions with LegionShip
    - vice_officer for All Missions with LegionShip Weapons, Shields, Medial, Engines under Life Support
    - tactical_officer for Battle Missions and LegionShip Weapons, Mess Hall, LegionShip Simulator
    - science_officer for Science Missions and LegionShip Shields, LegionShip Farms, Science Labs
    - medical_officer for All Missions and LegionShip Medical, LegionShip Quarters, Medical Labs
    - engineer_officer for Trade Missions and LegionShip Engines, Life Support, Engineer Labs 

Thus we get

- BridgeConfig:
    - lead_officer of ship bridge
    - vice_officer of ship systems
    - first_officer of tactical systems
    - second_officer of science systems
    - third_officer of medical systems
    - fourth_officer of engineering systems

- ShipLayout:
    - UpperDeck: Bridge Deck
        - Bridge: of lead_officers
        - Meeting Room: War Room
    - MidUpperDeck: Battle Deck
        - LegionShip Shields: of 1, 2, 3, 4 shield slots with Science Officers
        - LegionShip Hanger: of space-speeders in space-squadrons
        - LegionShip Weapons: of 2, 4, 6, 8 gun slots with Tactical Officers
    - MidDeck: Habitat Deck
        - LegionShip Quarters: Officer's Quarters and Quarter Exam
        - LegionShip Lab: Medical, Engineer, Tactical and Science Officers and Lab Exams
        - LegionShip Mess Hall: LegionShip's kitchen and LegionShip's farm
            - LegionShip Hall: Crew Cafeteria and meeting area
            - LegionShip Farm: LegionShip's Food source for ship survival and crew mood
            - LegionShip Bar: LegionShip's Adult Crew socializing for hangouts and dates
            - LegionShip Simulator: Social and Tactical Exams
                - LegionFleet Battles
                - Base Battles
                - Orbit Battles => LegionFleet vs Base
    - LowerDeck: Engineering Deck
        - LegionShip Life Support: Engineer Officers
        - LegionShip Engines: Engineer Officers

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
            medical_officer: PrismDrone,
            crew: list
    ):
        self.id = lead_officer.id

        self.lead_officer = lead_officer
        self.vice_officer = vice_officer
        self.tactical_officer = tactical_officer
        self.science_officer = science_officer
        self.engineer_officer = engineer_officer
        self.medical_officer = medical_officer

        ship_crew = [
            self.lead_officer,
            self.vice_officer,
            self.tactical_officer,
            self.engineer_officer,
            self.science_officer,
            self.medical_officer
        ]
        crew_ids = set([ship_member.id for ship_member in ship_crew])
        for ship_member in crew:
            if ship_member.id in crew_ids:
                continue
            ship_crew.append(ship_member)
        self.crew = ship_crew

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

        self.layout[1] = {
            "hanger": { "speeders": {}, "fighters": {}, "shuttles": {} },
            "shields": { "energy": {}, "armor": {}, "hull": {}},
            "weapons": { "cannons": {}, "launchers": {}, "turrets": {} }
        }

        quarters = { leader.id: { "room": [] } for leader in self.leaders() }
        for ship_member in self.crew:
            if ship_member.id in quarters:
                continue
            quarters[ship_member.id] = { "room": [ship_member] }

        lab = {
            "medical_labs": { medical_officer.id: { } },
            "science_labs": { science_officer.id: { } },
            "engineer_labs": { engineer_officer.id: { } },
            "tactical_labs": { tactical_officer.id: { } }
        }
        hall = {
            "kitchen": {},
            "hall": {},
            "bar": {},
            "simulator": {}
        }
        self.layout[2] = {
            "quarters": quarters,
            "lab": lab,
            "hall": hall
        }

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
            "engines": engines,
            "life_support": life_support,
            "cargo": cargo
        }

    def leaders(self):
        return self.layout[0].values()



class StarCruiser(StarShip): # Outposts, Camps
    def __init__(
            self,
            lead_officer: PrismDrone,
            vice_officer: PrismDrone,
            tactical_officer: PrismDrone,
            science_officer: PrismDrone,
            engineer_officer: PrismDrone,
            medical_officer: PrismDrone,
            crew: list
    ):
        super().__init__(
            lead_officer,
            vice_officer,
            tactical_officer,
            science_officer,
            engineer_officer,
            medical_officer,
            crew
        )


class StarFrigate(StarShip): # Town, Outposts
    def __init__(
            self,
            lead_officer: PrismDrone,
            vice_officer: PrismDrone,
            tactical_officer: PrismDrone,
            science_officer: PrismDrone,
            engineer_officer: PrismDrone,
            medical_officer: PrismDrone,
            crew: list
    ):
        super().__init__(
            lead_officer,
            vice_officer,
            tactical_officer,
            science_officer,
            engineer_officer,
            medical_officer,
            crew
        )


class StarCapital(StarShip): # City, Town
    def __init__(
            self,
            lead_officer: PrismDrone,
            vice_officer: PrismDrone,
            tactical_officer: PrismDrone,
            science_officer: PrismDrone,
            engineer_officer: PrismDrone,
            medical_officer: PrismDrone,
            crew: list
    ):
        super().__init__(
            lead_officer,
            vice_officer,
            tactical_officer,
            science_officer,
            engineer_officer,
            medical_officer,
            crew
        )


class StarDreadnought(StarShip): # Citadel
    def __init__(
            self,
            lead_officer: PrismDrone,
            vice_officer: PrismDrone,
            tactical_officer: PrismDrone,
            science_officer: PrismDrone,
            engineer_officer: PrismDrone,
            medical_officer: PrismDrone,
            crew: list
    ):
        super().__init__(
            lead_officer,
            vice_officer,
            tactical_officer,
            science_officer,
            engineer_officer,
            medical_officer,
            crew
        )

