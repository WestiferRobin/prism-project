from configs.game_config import TILE_WIDTH, TILE_HEIGHT
from utils.fotf_utils.game_utils.map_utils import generate_tile_map  # wherever your generator is

class MapManager:
    def __init__(self, game):
        self.game = game
        self.tile_map = generate_tile_map()

        # Calculate the map's pixel size
        self.map_pixel_width = len(self.tile_map[0]) * TILE_WIDTH
        self.map_pixel_height = len(self.tile_map) * TILE_HEIGHT

    def get_tile(self, x, y):
        if 0 <= y < len(self.tile_map) and 0 <= x < len(self.tile_map[0]):
            return self.tile_map[y][x]
        return None

    def draw(self, screen, selected_tile=None, hovered_tile=None):
        for row in self.tile_map:
            for tile in row:
                tile.draw(
                    screen,
                    self.game,
                    selected=(selected_tile == (tile.x, tile.y)),
                    hovered_tile=hovered_tile
                )