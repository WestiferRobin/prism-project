import pygame

class CameraManager:
    def __init__(self, speed=20):
        self.offset = [0, 0]
        self.speed = speed
        self.zoom = 1.0  # Default zoom level

    def handle_movement_keys(self):
        keys = pygame.key.get_pressed()

        dy = (keys[pygame.K_w] - keys[pygame.K_s]) * self.speed
        dx = (keys[pygame.K_a] - keys[pygame.K_d]) * self.speed
        self.offset[0] += dx
        self.offset[1] += dy

    def apply(self, rect_or_pos):
        """Apply camera offset and zoom to rects or (x, y) tuples."""
        if isinstance(rect_or_pos, pygame.Rect):
            new_rect = rect_or_pos.move(self.offset)
            return pygame.Rect(
                new_rect.x * self.zoom,
                new_rect.y * self.zoom,
                new_rect.width * self.zoom,
                new_rect.height * self.zoom
            )
        elif isinstance(rect_or_pos, (tuple, list)):
            return (
                (rect_or_pos[0] + self.offset[0]) * self.zoom,
                (rect_or_pos[1] + self.offset[1]) * self.zoom
            )

    def zoom_in(self, amount=0.05):
        self.zoom = min(2.0, self.zoom + amount)

    def zoom_out(self, amount=0.05):
        self.zoom = max(0.5, self.zoom - amount)
