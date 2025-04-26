from configs.game_config import TILE_WIDTH, TILE_HEIGHT, MAP_HEIGHT, MAP_WIDTH
from models.fotf.tiles.model import TerrainType, Tile


def screen_to_tile(mouse_x, mouse_y, game):
    zoom = game.game_manager.camera_manager.zoom
    offset_x, offset_y = game.game_manager.camera_manager.offset

    screen_width, screen_height = game.screen.get_size()
    map_pixel_width = game.game_manager.map_manager.map_pixel_width
    map_pixel_height = game.game_manager.map_manager.map_pixel_height

    start_x = (screen_width // 2) - (map_pixel_width // 2) + offset_x
    start_y = (screen_height // 2) - (map_pixel_height // 2) + offset_y

    world_x = (mouse_x - start_x) / zoom
    world_y = (mouse_y - start_y) / zoom

    tile_x = int(world_x // TILE_WIDTH)
    tile_y = int(world_y // TILE_HEIGHT)

    return tile_x, tile_y



def generate_tile_map():
    tile_map = []
    terrain = TerrainType.STONE

    for y in range(MAP_HEIGHT):
        row = []
        for x in range(MAP_WIDTH):
            tile = Tile(x, y, terrain, 1)
            row.append(tile)
        tile_map.append(row)

    return tile_map
