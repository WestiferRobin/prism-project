import pygame

from configs.game_config import MAP_WIDTH, MAP_HEIGHT
from utils.fotf_utils.game_utils.view_utils import screen_to_tile


class InputManager:
    def __init__(self, game):
        self.game = game

    def handle_mouse(self, event):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        tile_x, tile_y = screen_to_tile(mouse_x, mouse_y, self.game)
        tile_x = max(0, min(MAP_WIDTH - 1, tile_x))
        tile_y = max(0, min(MAP_HEIGHT - 1, tile_y))
        self.game.debug_selected_tile = (tile_x, tile_y)

        units = self.game.game_manager.unit_manager.units
        targets = self.game.game_manager.unit_manager.unit_targets
        selected_indexes = self.game.game_manager.selection_manager.selected_unit_indexes

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i, unit in enumerate(units):
                    if int(unit[0]) == tile_x and int(unit[1]) == tile_y:
                        self.game.game_manager.selection_manager.selected_unit_indexes = [i]
                        return
                if selected_indexes:
                    for i in selected_indexes:
                        targets[i] = [tile_x, tile_y]
                else:
                    self.game.game_manager.selection_manager.start_selection(pygame.mouse.get_pos())

            elif event.button == 3:
                if not any(int(unit[0]) == tile_x and int(unit[1]) == tile_y for unit in units):
                    selected_indexes.clear()

        elif event.type == pygame.MOUSEMOTION and self.game.game_manager.selection_manager.drag_start:
            self.game.game_manager.selection_manager.update_selection(pygame.mouse.get_pos())

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.game.game_manager.selection_manager.selection_box:
                self.game.game_manager.selection_manager.finalize_selection(self.game.game_manager.unit_manager)

    def handle_keys(self):
        self.game.game_manager.camera_manager.handle_keys()
