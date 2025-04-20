import pygame

from configs.game_config import FotfConfig

from models.fotf.managers.camera_manager import CameraManager
from models.fotf.managers.input_manager import InputManager
from models.fotf.managers.selection_manager import SelectionManager
from models.fotf.managers.unit_manager import UnitManager
from utils.fotf_utils.game_utils.map_utils import generate_tile_map
from utils.fotf_utils.game_utils.render_utils import render_selection_box, render_units, render_grid
from utils.fotf_utils.game_utils.update_utils import update_units


class FotfGame:
    def __init__(self):
        pygame.init()
        self.config = FotfConfig()

        self.screen = pygame.display.set_mode(
            (pygame.display.Info().current_w, pygame.display.Info().current_h),
            pygame.RESIZABLE
        )

        self.clock = pygame.time.Clock()
        self.window_width, self.window_height = self.screen.get_size()

        self.running = True
        self.camera = CameraManager()
        self.input_manager = InputManager(self)

        self.tile_map = generate_tile_map()
        self.unit_manager = UnitManager(units=[[5, 5]], speed=0.125)
        self.selection_manager = SelectionManager()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.running = False
            else:
                self.input_manager.handle_mouse(event)
        self.input_manager.handle_keys()

    def update(self):
        update_units(self)

    def render(self):
        self.screen.fill((0, 0, 0))
        render_grid(self)
        render_units(self)
        render_selection_box(self)
        pygame.display.flip()


def run_fotf():
    FotfGame().run()
