from src.models.bases.legion_base import LegionBase
from src.models.legions.armada import LegionArmada
from src.models.legions.legionfleet import LegionFleet
from src.models.legions.legion import Legion
from src.models.ships.model import LegionShip


def example_population():
    fleet_population = {
        "fleet_id": "",
        "base_ids": [],
        "ship_ids": []
    }
    for fleet_id in self.fleets():
        fleet = self.fleets()[fleet_id]
        fleet_entry = {
            "fleet_id": fleet_id
        }
    base_population = {
        "fleet_ids": []
    }
    ship_population = {
        "ship_id": "",
        "bridge_crew_ids": {
            "lead_id": "",
            "vice_id": "",
            "tactical_id": "",
            "science_id": "",
            "medical_id": "",
            "engineer_id": ""
        },
        "crew_ids": [],
    }
    prism_population = {}

    return {
        "prisms": prism_population
    }

def build_legion_population(legion: Legion):
    pass

def build_armada_population(armada: LegionArmada):
   for fleet in armada.fleets().values():
       build_fleet_population(fleet)

def build_fleet_population(fleet: LegionFleet):
    for ship in fleet.ships().values():
        build_ship_population(ship)
        build_ship_population(ship.home_base())

def build_ship_population(ship: LegionShip):
    crew = ship.crew()


def build_base_population(base: LegionBase):
    houses = base.houses()

def build_prism_population(prisms: tuple):


def build_squadron_population():
    """
    show all the workers on ships and bases including troopers and managers and leaders
    """
    pass

def build_family_population():
    """
    show all the families on legion bases
    """
    pass

def build_academy_population():
    """
    show all the children in legion academies
    """
    pass
