
def find_fleet_ship(fleet, ship_id):
    if ship_id not in fleet.ships:
        return None
    ship = fleet.ships[ship_id]
    return ship


def find_fleet_ships_by_type(fleet, ship_type: type):
    ships = []
    for ship in fleet.ships():
        if type(ship) == ship_type:
            ships.append(ship)
    return tuple(ships)