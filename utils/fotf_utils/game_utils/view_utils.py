from configs.game_config import MAP_WIDTH, MAP_HEIGHT, TILE_WIDTH, TILE_HEIGHT

def iso_coords(x, y, game):
    map_pixel_width = (MAP_WIDTH + MAP_HEIGHT) * TILE_WIDTH // 2
    map_pixel_height = (MAP_WIDTH + MAP_HEIGHT) * TILE_HEIGHT // 2
    offset_x = (game.window_width - map_pixel_width) // 2 + game.camera_offset[0]
    offset_y = (game.window_height - map_pixel_height) // 2 + game.camera_offset[1]
    screen_x = (x - y) * TILE_WIDTH // 2 + offset_x + map_pixel_width // 2
    screen_y = (x + y) * TILE_HEIGHT // 2 + offset_y
    return screen_x, screen_y

def screen_to_tile(screen_x, screen_y, game):
    map_pixel_width = (MAP_WIDTH + MAP_HEIGHT) * TILE_WIDTH // 2
    map_pixel_height = (MAP_WIDTH + MAP_HEIGHT) * TILE_HEIGHT // 2
    offset_x = (game.window_width - map_pixel_width) // 2 + game.camera_offset[0]
    offset_y = (game.window_height - map_pixel_height) // 2 + game.camera_offset[1]
    offset_x += map_pixel_width // 2

    temp_x = screen_x - offset_x
    temp_y = screen_y - offset_y

    raw_tile_x = ((temp_y / (TILE_HEIGHT / 2)) + (temp_x / (TILE_WIDTH / 2))) / 2
    raw_tile_y = ((temp_y / (TILE_HEIGHT / 2)) - (temp_x / (TILE_WIDTH / 2))) / 2

    tile_x = int(raw_tile_x-0.5)
    tile_y = int(raw_tile_y+0.5)
    return tile_x, tile_y