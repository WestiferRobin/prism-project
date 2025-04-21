import pygame


class CameraManager:
    def __init__(self, speed=20):
        self.offset = [0, 0]
        self.speed = speed

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: self.offset[1] += self.speed
        if keys[pygame.K_s]: self.offset[1] -= self.speed
        if keys[pygame.K_a]: self.offset[0] += self.speed
        if keys[pygame.K_d]: self.offset[0] -= self.speed
