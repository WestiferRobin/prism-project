import pygame

from configs.game_config import TILE_WIDTH, TILE_HEIGHT, MAP_HEIGHT, MAP_WIDTH
from utils.fotf_utils.game_utils.view_utils import iso_coords


def render_selection_box(game):
    if not game.selection_manager.selection_box:
        return
    pygame.draw.rect(game.screen, (0, 255, 255), game.selection_manager.selection_box, 1)


def render_units(game):
    for i, unit in enumerate(game.unit_manager.units):
        screen_x, screen_y = iso_coords(*unit, game)
        center_x = screen_x + TILE_WIDTH // 2
        center_y = screen_y + TILE_HEIGHT // 2
        pygame.draw.circle(game.screen, (0, 200, 255), (center_x, center_y), 10)
        if game.unit_manager.is_selected(i, game.selection_manager):
            pygame.draw.circle(game.screen, (255, 255, 0), (center_x, center_y), 14, 2)


def render_grid(game):
    target_tiles = set(tuple(v) for v in game.unit_manager.unit_targets.values())
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            screen_pos = iso_coords(x, y, game)
            terrain = game.tile_map[y][x]

            if (x, y) in target_tiles:
                color = (255, 255, 0)
            elif terrain == "water":
                color = (0, 0, 255)
            elif terrain == "forest":
                color = (34, 139, 34)
            else:
                color = (100, 100, 100)

            points = [
                (screen_pos[0], screen_pos[1] + TILE_HEIGHT // 2),
                (screen_pos[0] + TILE_WIDTH // 2, screen_pos[1]),
                (screen_pos[0] + TILE_WIDTH, screen_pos[1] + TILE_HEIGHT // 2),
                (screen_pos[0] + TILE_WIDTH // 2, screen_pos[1] + TILE_HEIGHT),
            ]
            pygame.draw.polygon(game.screen, color, points)

            if hasattr(game, "debug_selected_tile") and (x, y) == game.debug_selected_tile:
                pygame.draw.polygon(game.screen, (255, 255, 0), points, 5)  # Yellow border
            else:
                pygame.draw.polygon(game.screen, (50, 50, 50), points, 1)