import pygame
from configs.game_config import (
    WINDOW_WIDTH, WINDOW_HEIGHT,
    TILE_WIDTH, TILE_HEIGHT,
    MAP_WIDTH, MAP_HEIGHT
)
# from src.models.legions.model import AdminLegion
# from src.models.solars.galaxy import UniverseGalaxy

class Game:
    def __init__(self, name: str):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(name)
        self.clock = pygame.time.Clock()
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

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
        pygame.quit()


class Fotf(Game):
    def __init__(self):
        super().__init__("FotF")
        # self.board = UniverseGalaxy()
        # self.player_faction = AdminLegion("Federation")
        # self.enemy_faction = AdminLegion("Empire")
        self.selector = None
        self.tilemap = self.generate_tilemap()

    def generate_tilemap(self):
        tilemap = []
        for y in range(MAP_HEIGHT):
            row = []
            for x in range(MAP_WIDTH):
                if x == 3 and y == 2:
                    row.append("resource")
                elif x == 5 and y == 5:
                    row.append("building")
                elif x == 7 and y == 4:
                    row.append("unit")
                else:
                    row.append("grass")
            tilemap.append(row)
        return tilemap

    def iso_coords(self, x, y):
        screen_x = (x - y) * TILE_WIDTH // 2 + WINDOW_WIDTH // 2
        screen_y = (x + y) * TILE_HEIGHT // 2
        return screen_x, screen_y

    def get_tile_from_screen(self, screen_x, screen_y):
        dx = screen_x - WINDOW_WIDTH // 2
        dy = screen_y

        x = (dy / TILE_HEIGHT + dx / TILE_WIDTH)
        y = (dy / TILE_HEIGHT - dx / TILE_WIDTH)

        x = int(x // 2)
        y = int(y // 2)

        if 0 <= x < MAP_WIDTH and 0 <= y < MAP_HEIGHT:
            return x, y
        return None

    def handle_events(self):
        super().handle_events()
        if pygame.mouse.get_pressed()[0]:  # Left click
            mouse_x, mouse_y = pygame.mouse.get_pos()
            tile = self.get_tile_from_screen(mouse_x, mouse_y)
            if tile:
                self.selector = tile

    def draw_grid(self):
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                screen_pos = self.iso_coords(x, y)
                tile_type = self.tilemap[y][x]

                if tile_type == "grass":
                    color = (34, 139, 34)  # Green
                elif tile_type == "resource":
                    color = (0, 191, 255)  # Blue
                elif tile_type == "building":
                    color = (169, 169, 169)  # Gray
                elif tile_type == "unit":
                    color = (255, 215, 0)  # Gold
                else:
                    color = (255, 255, 255)

                points = [
                    (screen_pos[0], screen_pos[1] + TILE_HEIGHT // 2),
                    (screen_pos[0] + TILE_WIDTH // 2, screen_pos[1]),
                    (screen_pos[0] + TILE_WIDTH, screen_pos[1] + TILE_HEIGHT // 2),
                    (screen_pos[0] + TILE_WIDTH // 2, screen_pos[1] + TILE_HEIGHT),
                ]
                pygame.draw.polygon(self.screen, color, points)

        if self.selector:
            sel_x, sel_y = self.selector
            screen_pos = self.iso_coords(sel_x, sel_y)
            points = [
                (screen_pos[0], screen_pos[1] + TILE_HEIGHT // 2),
                (screen_pos[0] + TILE_WIDTH // 2, screen_pos[1]),
                (screen_pos[0] + TILE_WIDTH, screen_pos[1] + TILE_HEIGHT // 2),
                (screen_pos[0] + TILE_WIDTH // 2, screen_pos[1] + TILE_HEIGHT),
            ]
            pygame.draw.polygon(self.screen, (255, 0, 0), points, 2)

    def draw(self):
        super().draw()
        self.draw_grid()

"""
THIS IS AN RTS GAME ON DIFFERENT DIMENSIONS. COLLECT TRADE AND FIGHT. thats the game. a game for the masculine spirit
"""
def run_fotf():
    Fotf().run()
