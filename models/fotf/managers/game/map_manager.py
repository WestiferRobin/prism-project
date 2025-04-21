from configs.game_config import MAP_HEIGHT, MAP_WIDTH, TILE_WIDTH, TILE_HEIGHT
import random
import pygame

from models.fotf.tiles.model import Tile, TerrainType, BlockType
from utils.fotf_utils.game_utils.view_utils import iso_coords

def generate_tile_map():
    tile_map = []
    for y in range(MAP_HEIGHT):
        row = []
        for x in range(MAP_WIDTH):
            terrain = TerrainType.STONE
            elevation = 1
            block_type = BlockType.FLAT
            tile = Tile(x, y, terrain, elevation)
            tile.block = block_type
            row.append(tile)
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
        tile = self.get_tile(x, y)
        if not tile:
            return 0, 0, 0
        elif highlight:
            return 255, 255, 0

        terrain_color_map = {
            TerrainType.GRASS: (0, 255, 0),
            TerrainType.DIRT: (139, 69, 19),
            TerrainType.WATER: (0, 0, 255),
            TerrainType.STONE: (120, 120, 120),
            TerrainType.DESERT: (237, 201, 175),
            TerrainType.SNOW: (255, 255, 255),
        }

        return terrain_color_map.get(tile.terrain, (100, 100, 100))

    def draw_tile(self, screen, x, y, selected=False, debug_tile=None):
        screen_pos = iso_coords(x, y, self.game)
        tile = self.get_tile(x, y)
        elevation = tile.elevation if tile else 0
        block_height = TILE_HEIGHT
        color = self.get_tile_color(x, y, selected)
        base_y = screen_pos[1] + TILE_HEIGHT // 2

        # Draw full block stack
        for level in range(elevation):
            z_offset = block_height * level
            top = [
                (screen_pos[0], base_y - z_offset),
                (screen_pos[0] + TILE_WIDTH // 2, base_y - TILE_HEIGHT // 2 - z_offset),
                (screen_pos[0] + TILE_WIDTH, base_y - z_offset),
                (screen_pos[0] + TILE_WIDTH // 2, base_y + TILE_HEIGHT // 2 - z_offset)
            ]
            left = [
                (top[0][0], top[0][1]),
                (top[3][0], top[3][1]),
                (top[3][0], top[3][1] + block_height),
                (top[0][0], top[0][1] + block_height)
            ]
            right = [
                (top[3][0], top[3][1]),
                (top[2][0], top[2][1]),
                (top[2][0], top[2][1] + block_height),
                (top[3][0], top[3][1] + block_height)
            ]

            pygame.draw.polygon(screen, (max(color[0] - 40, 0), max(color[1] - 40, 0), max(color[2] - 40, 0)), left)
            pygame.draw.lines(screen, (0, 0, 0), True, left, 1)
            pygame.draw.polygon(screen, (max(color[0] - 20, 0), max(color[1] - 20, 0), max(color[2] - 20, 0)), right)
            pygame.draw.lines(screen, (0, 0, 0), True, right, 1)
            pygame.draw.polygon(screen, color, top)
            pygame.draw.lines(screen, (0, 0, 0), True, top, 1)

            if debug_tile and (x, y) == debug_tile:
                pygame.draw.polygon(screen, (255, 255, 0), top, 5)
            else:
                pygame.draw.polygon(screen, (50, 50, 50), top, 1)

