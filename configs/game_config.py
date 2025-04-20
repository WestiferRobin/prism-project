import pygame

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

TILE_WIDTH = 64
TILE_HEIGHT = 32

MAP_WIDTH = 10
MAP_HEIGHT = 10

class FotfConfig:
    def __init__(self):
        self.name = "FotF"
        pygame.display.set_caption(self.name)