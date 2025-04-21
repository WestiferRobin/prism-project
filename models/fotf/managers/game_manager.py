import pygame

from configs.game_config import MAP_HEIGHT, MAP_WIDTH
from models.fotf.managers.game.map_manager import MapManager
from models.fotf.managers.game.selection_manager import SelectionManager
from models.fotf.managers.game.unit_manager import UnitManager
from models.fotf.managers.input.camera_manager import CameraManager
from models.fotf.managers.input.input_manager import InputManager


class GameManager:
    def __init__(self, game):
        self.game = game
        self.camera_manager = CameraManager()
        self.input_manager = InputManager(self.game)
        self.map_manager = MapManager(self.game)
        self.selection_manager = SelectionManager()
        self.unit_manager = UnitManager(self.game, units=[[5, 5]], speed=0.125)
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.running = False
            else:
                self.input_manager.handle_mouse(event)
        self.input_manager.handle_keys()

    def update(self):
        self.unit_manager.update_units()

    def render(self):
        self.game.screen.fill((0, 0, 0))
        self._render_grid()
        self._render_units()
        self._render_selection_box()
        pygame.display.flip()

    def _render_grid(self):
        target_tiles = set(tuple(v) for v in self.unit_manager.unit_targets.values())
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                is_target = (x, y) in target_tiles
                self.map_manager.draw_tile(
                    self.game.screen, x, y, selected=is_target, debug_tile=getattr(self.game, "debug_selected_tile", None)
                )

    def _render_units(self):
        self.unit_manager.render()

    def _render_selection_box(self):
        self.selection_manager.render(self.game.screen)