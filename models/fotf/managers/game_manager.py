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

        # Managers
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

            # Handle zoom keys
            if event.type == pygame.KEYDOWN:
                self.input_manager.handle_zoom(event)

        # Continuous movement
        self.input_manager.handle_keys()

    def update(self):
        # Update unit movement, pathfinding, AI logic
        # self.unit_manager.update_units()
        pass

    def render(self):
        self.game.screen.fill((0, 0, 0))  # Clear screen with black

        # Draw order matters: Map first → Units → UI
        self._render_map()
        # self._render_units()
        # self._render_selection_box()

        pygame.display.flip()

    def _render_map(self):
        hovered_tile = getattr(self.game, "hovered_tile", None)

        self.map_manager.draw(
            screen=self.game.screen,
            selected_tile=None,
            hovered_tile=hovered_tile
        )

    # def _render_units(self):
    #     self.unit_manager.render()
    #
    # def _render_selection_box(self):
    #     self.selection_manager.render(self.game.screen)
