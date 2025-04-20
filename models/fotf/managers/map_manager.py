
class MapManager:
    def __init__(self, tile_map):
        self.tile_map = tile_map

    def get_tile(self, x, y):
        if 0 <= y < len(self.tile_map) and 0 <= x < len(self.tile_map[0]):
            return self.tile_map[y][x]
        return None

    def set_tile(self, x, y, value):
        if 0 <= y < len(self.tile_map) and 0 <= x < len(self.tile_map[0]):
            self.tile_map[y][x] = value

