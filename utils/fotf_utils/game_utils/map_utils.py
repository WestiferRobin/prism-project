from configs.game_config import MAP_HEIGHT, MAP_WIDTH


def generate_tile_map():
    from random import random
    tile_map = []
    for y in range(MAP_HEIGHT):
        row = []
        for x in range(MAP_WIDTH):
            r = random()
            if r < 0.1:
                row.append("water")
            elif r < 0.2:
                row.append("forest")
            else:
                row.append("grass")
        tile_map.append(row)
    return tile_map
