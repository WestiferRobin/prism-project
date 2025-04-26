from enum import Enum
import pygame
from configs.game_config import TILE_WIDTH, TILE_HEIGHT

class TerrainType(Enum):
    GRASS = "grass"
    DIRT = "dirt"
    WATER = "water"
    STONE = "stone"
    DESERT = "desert"
    SNOW = "snow"

class Tile:
    def __init__(self, x, y, terrain_type: TerrainType, elevation=1):
        self.x = x
        self.y = y
        self.terrain = terrain_type
        self.elevation = elevation

    def draw(self, screen, game, selected=False, hovered_tile=None):
        zoom = game.game_manager.camera_manager.zoom

        offset_x, offset_y = game.game_manager.camera_manager.offset
        screen_width, screen_height = game.screen.get_size()
        map_pixel_width = game.game_manager.map_manager.map_pixel_width
        map_pixel_height = game.game_manager.map_manager.map_pixel_height

        start_x = (screen_width // 2) - (map_pixel_width // 2) + offset_x
        start_y = (screen_height // 2) - (map_pixel_height // 2) + offset_y

        tile_size = TILE_WIDTH * zoom

        screen_x = start_x + self.x * tile_size
        screen_y = start_y + self.y * tile_size

        rect = pygame.Rect(screen_x, screen_y, tile_size, tile_size)

        # Base color with elevation shading
        color = self.get_color(selected)
        shade = min(self.elevation * 10, 50)
        shaded_color = tuple(max(c - shade, 0) for c in color)

        pygame.draw.rect(screen, shaded_color, rect)

        # Tile border
        border_thickness = max(1, int(1 * zoom))
        pygame.draw.rect(screen, (0, 0, 0), rect, border_thickness)

        # Mouse hover highlight
        if hovered_tile and (self.x, self.y) == hovered_tile:
            highlight_thickness = max(2, int(3 * zoom))
            pygame.draw.rect(screen, (255, 255, 0), rect, highlight_thickness)

    def get_color(self, selected):
        if selected:
            return (255, 255, 0)

        terrain_colors = {
            TerrainType.GRASS: (0, 255, 0),
            TerrainType.DIRT: (139, 69, 19),
            TerrainType.WATER: (0, 0, 255),
            TerrainType.STONE: (120, 120, 120),
            TerrainType.DESERT: (237, 201, 175),
            TerrainType.SNOW: (255, 255, 255),
        }
        return terrain_colors.get(self.terrain, (100, 100, 100))
