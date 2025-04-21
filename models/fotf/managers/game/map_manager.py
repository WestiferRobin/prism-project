from configs.game_config import MAP_HEIGHT, MAP_WIDTH, TILE_WIDTH, TILE_HEIGHT
import random
import pygame
from utils.fotf_utils.game_utils.view_utils import iso_coords

def generate_tile_map():
    tile_map = []
    for y in range(MAP_HEIGHT):
        row = []
        for x in range(MAP_WIDTH):
            r = random.random()
            if r < 0.1:
                row.append("water")
            elif r < 0.2:
                row.append("forest")
            else:
                row.append("grass")
        tile_map.append(row)
    return tile_map

class MapManager:
    def __init__(self, game):
        self.game = game
        self.tile_map = generate_tile_map()

    def get_tile(self, x, y):
        if 0 <= y < len(self.tile_map) and 0 <= x < len(self.tile_map[0]):
            return self.tile_map[y][x]
        return None

    def get_tile_color(self, x, y, highlight=False):
        terrain = self.get_tile(x, y)
        if highlight:
            return 255, 255, 0
        if terrain == "water":
            return 0, 0, 255
        elif terrain == "forest":
            return 34, 139, 34
        return 100, 100, 100

    def draw_tile(self, screen, x, y, selected=False, debug_tile=None):
        screen_pos = iso_coords(x, y, self.game)
        color = self.get_tile_color(x, y, selected)

        points = [
            (screen_pos[0], screen_pos[1] + TILE_HEIGHT // 2),
            (screen_pos[0] + TILE_WIDTH // 2, screen_pos[1]),
            (screen_pos[0] + TILE_WIDTH, screen_pos[1] + TILE_HEIGHT // 2),
            (screen_pos[0] + TILE_WIDTH // 2, screen_pos[1] + TILE_HEIGHT),
        ]

        pygame.draw.polygon(screen, color, points)
        if debug_tile and (x, y) == debug_tile:
            pygame.draw.polygon(screen, (255, 255, 0), points, 5)
        else:
            pygame.draw.polygon(screen, (50, 50, 50), points, 1)
