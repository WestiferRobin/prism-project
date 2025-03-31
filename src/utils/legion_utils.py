from src.models.legions.model import Legion
from src.utils.armada_utils import find_armada_fleet


def find_legion_drone(legion: Legion, drone_id):
    for prism in legion.drones():
        if prism.id == drone_id:
            return prism
    return None

def find_legion_leader(legion: Legion, leader_id):
    for leader in legion.leaders():
        if leader.id == leader_id:
            return leader
    return None

def find_legion_ship(legion: Legion, fleet_id, ship_id):
    fleet = find_legion_fleet(legion, fleet_id)
    if fleet is None:
        return None
    if ship_id not in fleet.ships():
        return None
    ship = fleet.ships()[ship_id]
    return ship

def find_legion_base(legion: Legion, base_id):
    for base in legion.bases():
        if base.id == base_id:
            return base
    return None

def find_legion_fleet(legion: Legion, fleet_id):
    fleet = find_armada_fleet(legion.armada, fleet_id)
    return fleet

def find_legion_solar(legion: Legion, solar_id):
    solars = legion.solars()
    for solar in solars:
        if solar.id == solar_id:
            return solar
    return None

def find_legion_planet(legion: Legion, planet_id):
    planets = legion.planets()
    for planet in planets:
        if planet.id == planet_id:
            return planet
    return None

def find_legion_moon(legion: Legion, moon_id):
    moons = legion.moons()
    for moon in moons:
        if moon.id == moon_id:
            return moon
    return None

def find_fleet_leaders(legion: Legion, leader_id, vice_id):
    leader = find_legion_leader(legion, leader_id)
    if leader is None:
        return None

    leaders = { leader_id: leader }
    primary_fleet = find_legion_fleet(legion, leader_id)
    secondary_fleet = find_legion_fleet(legion, vice_id)
    fleets = (primary_fleet, secondary_fleet)

    for fleet in fleets:
        for ship in fleet.ships():
            lead_officer = ship.lead_officer
            if lead_officer.id in leaders:
                continue
            leaders[lead_officer.id] = lead_officer

    return leaders

def find_base_leaders(legion: Legion, leader_id, vice_id):
    leader = find_legion_leader(legion, leader_id)
    if leader is None:
        return None

    leaders = {leader_id: leader}
    primary_fleet = find_legion_fleet(legion, leader_id)
    secondary_fleet = find_legion_fleet(legion, vice_id)
    fleets = (primary_fleet, secondary_fleet)

    for fleet in fleets:
        for ship in fleet.ships():
            home_base = ship.home_base()
            lead_officer = home_base.lead_officer
            if lead_officer.id in leaders:
                continue
            leaders[lead_officer.id] = lead_officer

    return leaders



