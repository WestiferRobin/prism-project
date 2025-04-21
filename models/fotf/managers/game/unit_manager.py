import pygame
from configs.game_config import TILE_WIDTH, TILE_HEIGHT
from utils.fotf_utils.game_utils.view_utils import iso_coords


class UnitManager:
    def __init__(self, game, units=None, speed=0.125):
        self.game = game
        self.units = units or []
        self.unit_speed = speed
        self.unit_targets = {}

    def update_units(self):
        for i, unit in enumerate(self.units):
            target = self.unit_targets.get(i)
            if target:
                dx = target[0] - unit[0]
                dy = target[1] - unit[1]
                dist = (dx**2 + dy**2) ** 0.5
                if dist < self.unit_speed:
                    self.units[i] = target
                    del self.unit_targets[i]
                else:
                    self.units[i][0] += self.unit_speed * dx / dist
                    self.units[i][1] += self.unit_speed * dy / dist

    def set_target_for_selected(self, selected_unit_indexes, target_pos):
        for i in selected_unit_indexes:
            self.unit_targets[i] = target_pos

    def is_selected(self, index):
        selection_manager = self.game.game_manager.selection_manager
        return selection_manager.is_selected(index)

    def render(self):
        for i, unit in enumerate(self.units):
            screen_x, screen_y = iso_coords(*unit, self.game)
            center_x = screen_x + TILE_WIDTH // 2
            center_y = screen_y + TILE_HEIGHT // 2
            pygame.draw.circle(self.game.screen, (0, 200, 255), (center_x, center_y), 10)
            if self.is_selected(i):
                pygame.draw.circle(self.game.screen, (255, 255, 0), (center_x, center_y), 14, 2)
