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

    def zoom_in(self, mouse_pos, amount=0.05):
        self.zoom_at(mouse_pos, amount)

    def zoom_out(self, mouse_pos, amount=0.05):
        self.zoom_at(mouse_pos, -amount)

    def zoom_at(self, mouse_pos, zoom_amount):
        old_zoom = self.zoom
        new_zoom = self.zoom + zoom_amount
        new_zoom = max(0.5, min(2.0, new_zoom))

        if new_zoom != old_zoom:
            mx, my = mouse_pos

            scale = new_zoom / old_zoom

            self.offset[0] = (self.offset[0] - mx) * scale + mx
            self.offset[1] = (self.offset[1] - my) * scale + my

            self.zoom = new_zoom

