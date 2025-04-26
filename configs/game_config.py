import pygame

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

TILE_SIZE = 64  # or 32, or whatever you want
TILE_WIDTH = TILE_SIZE
TILE_HEIGHT = TILE_SIZE

MAP_WIDTH = 10
MAP_HEIGHT = 10

class FotfConfig:
    def __init__(self):
        self.name = "FotF"
        pygame.display.set_caption(self.name)