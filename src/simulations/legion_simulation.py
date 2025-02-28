from src.models.legions.legion import AdminLegion, ArchLegion, Legion
from src.utils.armada_utils import find_armada_fleet


def simulate_legion(is_arch_legion: bool = False) -> Legion:
    name = "Legion"
    if is_arch_legion:
        return ArchLegion(name=name)
    else:
        return AdminLegion(name)

def simulate_armada(is_arch_legion: bool = False):
    legion = simulate_legion(is_arch_legion)
    return legion.armada

def simulate_fleet():
    legion_armada = simulate_armada(is_arch_legion=False)
    return find_armada_fleet(legion_armada, legion_armada.admin().id)

def simulate_star_ship(index: int):
    legion_fleet = simulate_fleet()
    star_ship = legion_fleet[index]
    return star_ship

def simulate_star_dreadnought():
    dreadnought = simulate_star_ship(0)
    return dreadnought

def simulate_star_capital(index: int=0):
    valid_index = index % 2
    if valid_index == 0:
        return simulate_star_capital(2)
    else:
        return simulate_star_capital(1)

def simulate_star_frigate(index: int=0):
    valid_index = index % 3
    if valid_index == 0:
        return simulate_star_ship(4)
    elif valid_index == 1:
        return simulate_star_ship(3)
    else:
        return simulate_star_ship(5)

def simulate_star_cruiser(index: int=0):
    valid_index = index % 4
    if valid_index == 0:
        return simulate_star_ship(9)
    elif valid_index == 1:
        return simulate_star_ship(6)
    elif valid_index == 2:
        return simulate_star_ship(7)
    else:
        return simulate_star_ship(8)

def simulate_space_shuttle(index: int):
    ship_index = index % 10
    if ship_index == 0:
        ship = simulate_star_dreadnought()
    elif 1 <= ship_index <= 2:
        ship = simulate_star_capital(ship_index)
    elif 3 <= ship_index <= 5:
        ship = simulate_star_frigate(ship_index)
    else:
        ship = simulate_star_cruiser(ship_index)
    shuttle = ship.hanger()["shuttle-squadrons"][0]
    return shuttle

def simulate_space_fighters(index: int):
    ship_index = index % 6
    if ship_index == 0:
        ship = simulate_star_dreadnought()
    elif 1 <= ship_index <= 2:
        ship = simulate_star_capital(ship_index)
    else:
        ship = simulate_star_frigate(ship_index)
    fighters = ship.hanger()["fighter-squadrons"][0]
    return fighters

def simulate_space_speeders(index: int):
    ship_index = index % 10
    if ship_index == 0:
        ship = simulate_star_dreadnought()
    elif 1 <= ship_index <= 2:
        ship = simulate_star_capital(ship_index)
    elif 3 <= ship_index <= 5:
        ship = simulate_star_frigate(ship_index)
    else:
        ship = simulate_star_cruiser(ship_index)
    speeders = ship.hanger()["speeder-squadrons"][0]
    return speeders



