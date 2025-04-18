import pygame
from configs.game_config import (
    TILE_WIDTH, TILE_HEIGHT,
    MAP_WIDTH, MAP_HEIGHT
)


class Game:
    def __init__(self, name: str):
        pygame.init()
        self.screen = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h), pygame.RESIZABLE)
        self.window_width, self.window_height = self.screen.get_size()
        pygame.display.set_caption(name)
        self.clock = pygame.time.Clock()
        self.running = True
        self.camera_offset = [0, 0]  # For panning the map
        self.last_move_time = pygame.time.get_ticks()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

        keys = pygame.key.get_pressed()
        cam_speed = 20

        if keys[pygame.K_w]:
            self.camera_offset[1] += cam_speed
        if keys[pygame.K_s]:
            self.camera_offset[1] -= cam_speed
        if keys[pygame.K_a]:
            self.camera_offset[0] += cam_speed
        if keys[pygame.K_d]:
            self.camera_offset[0] -= cam_speed

    def update(self):
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
        print("Exiting Fotf Game")
        pygame.quit()
