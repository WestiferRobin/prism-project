from src.models.legion import AdminLegion


def simulate_legion():
    return AdminLegion()

def simulate_armada():
    return simulate_legion().armada()

def simulate_fleet():
    legion_armada = simulate_armada()
    return legion_armada.fleets[legion_armada.leader]

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
    pass

def simulate_space_fighter(index: int):
    pass

def simulate_space_speeder(index: int):
    pass

def simulate_space_vehicle(index: int):
    pass


