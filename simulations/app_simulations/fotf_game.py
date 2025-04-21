import pygame

from configs.game_config import FotfConfig
from models.fotf.managers.game_manager import GameManager


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

        self.game_manager = GameManager(self)

    def run(self):
        while self.game_manager.running:
            self.game_manager.handle_events()
            self.game_manager.update()
            self.game_manager.render()
            self.clock.tick(60)
        pygame.quit()


def run_fotf():
    FotfGame().run()
