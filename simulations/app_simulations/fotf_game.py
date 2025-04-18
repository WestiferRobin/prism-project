import pygame
from configs.game_config import (
    WINDOW_WIDTH, WINDOW_HEIGHT,
    TILE_WIDTH, TILE_HEIGHT,
    MAP_WIDTH, MAP_HEIGHT
)

class Game:
    def __init__(self, name: str):
        pygame.init()
        self.screen = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h), pygame.RESIZABLE)
        global WINDOW_WIDTH, WINDOW_HEIGHT
        WINDOW_WIDTH, WINDOW_HEIGHT = self.screen.get_size()
        pygame.display.set_caption(name)
        self.clock = pygame.time.Clock()
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()
        move_x, move_y = 0, 0

        # 8-directional movement mapped for isometric logic
        if keys[pygame.K_w] and keys[pygame.K_d]:  # Up-Right
            move_x, move_y = 0, -1
        elif keys[pygame.K_w] and keys[pygame.K_a]:  # Up-Left
            move_x, move_y = -1, 0
        elif keys[pygame.K_s] and keys[pygame.K_d]:  # Down-Right
            move_x, move_y = 1, 0
        elif keys[pygame.K_s] and keys[pygame.K_a]:  # Down-Left
            move_x, move_y = 0, 1
        elif keys[pygame.K_w]:  # Up
            move_x, move_y =  -1, -1
        elif keys[pygame.K_s]:  # Down
            move_x, move_y = 1, 1
        elif keys[pygame.K_a]:  # Left
            move_x, move_y = -1, 1
        elif keys[pygame.K_d]:  # Right
            move_x, move_y = 1, -1

        # Add a cooldown to slow down movement speed
        if not hasattr(self, 'move_timer'):
            self.move_timer = 0

        if self.move_timer <= 0:
            new_x = max(0, min(MAP_WIDTH - 1, self.player_pos[0] + move_x))
            new_y = max(0, min(MAP_HEIGHT - 1, self.player_pos[1] + move_y))
            self.player_pos = [new_x, new_y]
            self.move_timer = 10  # frames between moves
        else:
            self.move_timer -= 1

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


class Fotf(Game):
    def __init__(self):
        super().__init__("FotF")
        self.selector = None
        self.tilemap = self.generate_tilemap()
        self.player_pos = [5, 5]

    def generate_tilemap(self):
        tilemap = []
        for y in range(MAP_HEIGHT):
            row = []
            for x in range(MAP_WIDTH):
                row.append("grass")
            tilemap.append(row)
        return tilemap

    def iso_coords(self, x, y):
        map_pixel_width = (MAP_WIDTH + MAP_HEIGHT) * TILE_WIDTH // 2
        map_pixel_height = (MAP_WIDTH + MAP_HEIGHT) * TILE_HEIGHT // 2
        offset_x = (WINDOW_WIDTH - map_pixel_width) // 2
        offset_y = (WINDOW_HEIGHT - map_pixel_height) // 2
        screen_x = (x - y) * TILE_WIDTH // 2 + offset_x + map_pixel_width // 2
        screen_y = (x + y) * TILE_HEIGHT // 2 + offset_y
        return screen_x, screen_y

    def draw_grid(self):
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                screen_pos = self.iso_coords(x, y)
                color = (34, 139, 34)
                points = [
                    (screen_pos[0], screen_pos[1] + TILE_HEIGHT // 2),
                    (screen_pos[0] + TILE_WIDTH // 2, screen_pos[1]),
                    (screen_pos[0] + TILE_WIDTH, screen_pos[1] + TILE_HEIGHT // 2),
                    (screen_pos[0] + TILE_WIDTH // 2, screen_pos[1] + TILE_HEIGHT),
                ]
                pygame.draw.polygon(self.screen, color, points)
                pygame.draw.polygon(self.screen, (50, 50, 50), points, 1)  # grid lines

    def draw_player(self):
        x, y = self.player_pos
        screen_x, screen_y = self.iso_coords(x, y)
        center_x = screen_x + TILE_WIDTH // 2
        center_y = screen_y + TILE_HEIGHT // 2
        pygame.draw.circle(self.screen, (255, 0, 0), (center_x, center_y), 10)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.draw_grid()
        self.draw_player()
        pygame.display.flip()

"""
THIS IS AN RTS GAME ON DIFFERENT DIMENSIONS. COLLECT TRADE AND FIGHT. thats the game. a game for the masculine spirit
"""
def run_fotf():
    Fotf().run()
