
import pygame

from src.models.drones.model import PrismDrone
from src.models.games.fotf_game import FotfGame

max_game_byte_size = 16

def run_fotf_game(avatar: PrismDrone):
    fotf_game = FotfGame(avatar)
    # Solve for nxm Room of n and m Tiles
    # Solve for 2x2 Room Battle with 2 Prisms of 1 team
    # Solve for 4x4 Room Battle with 4 Prisms of 1 or 2 teams
    # Solve for 8x8 Room Battle with 8 Prisms of 1 or 2 or 4 teams
    # Solve for 9x9 Room Battle with 9 Prisms of 1 or 3 teams
    # Solve for 16x16 Room Battle with 12 Prisms of 1 or 2 or 3 or 4 or 6 or 8 or 9 or 12 teams
    # Solve for 64x64 Rooms of Land and Orbit Tile Spaces for 16 Prisms of 1 StarCruiser

def run_game_simulations(avatar: PrismDrone):
    run_fotf_game(avatar)

"""
for visual game simulations
"""
def draw_board(board, screen, length: int, width: int):

    # Constants
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    MAGENTA = (255, 0, 255)
    RED = (255, 0, 0)
    CYAN = (0, 255, 255)
    GRAY = (128, 128, 128)

    screen.fill(BLACK)  # Fill background

    cell_size = 16
    for i in range(0, width):
        for j in range(0, length):
            white_band = (i + j) % 2 == 0
            red_band = (i + j) % 3 == 0
            blue_band = (i + j) % 4 == 0
            green_band = (i + j) % 6 == 0

            if white_band == 0:
                if red_band and blue_band and green_band:
                    color = GRAY
                elif red_band and not blue_band and not green_band:
                    color = CYAN
                elif not red_band and blue_band and not green_band:
                    color = YELLOW
                elif not red_band and not blue_band and green_band:
                    color = MAGENTA
                else:
                    color = WHITE
            else:
                if red_band and blue_band and green_band:
                    color = GRAY
                elif red_band and not blue_band and not green_band:
                    color = RED
                elif not red_band and blue_band and not green_band:
                    color = BLUE
                elif not red_band and not blue_band and green_band:
                    color = GREEN
                else:
                    color = BLACK

            pygame.draw.rect(screen, color, (i * cell_size, j * cell_size, cell_size, cell_size))

"""
for visual game simulations
"""
def create_board(length: int = 8, height: int = None):
    length = max(0, length)
    if height is None:
        height = max(0, length)

    board = [["." for _ in range(height)] for _ in range(length)]

    # Place pieces in initial positions
    # for row in range(length):
    return board

def run_visual_simulation(name: str=None):
    if name is None:
        name = "game-board"
    else:
        name = f"{name}'s game-board"

    # Initialize Pygame
    pygame.init()

    board = create_board()
    size = len(board)
    print(size)
    WIDTH = size**2
    HEIGHT = size**2
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(name)

    # Game Loop
    running = True

    while running:
        draw_board(board=board, screen=screen, width=WIDTH, length=HEIGHT)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

def run_room_visual_simulation():
    pass

def run_ship_visual_simulation():
    pass

def run_board_visual_simulation():
    pass


def run_game_simulation(has_ui=False):
    avatar = PrismDrone()
    if has_ui:
        run_visual_simulation()
    else:
        run_fotf_game(avatar)

if __name__ == "__main__":
    run_game_simulation(has_ui=True)
