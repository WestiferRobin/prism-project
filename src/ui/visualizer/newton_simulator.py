import pygame
import sys
import math

from src.physics.forces import Force
from src.physics.kinematics import KinematicMotion

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
FPS = 60
GRAVITY = 9.8

# Define mass and acceleration functions
mass = lambda t: 1
acceleration = [
    lambda t: -math.sin(t),     # spring-like force in x
    lambda t: GRAVITY           # gravity in y
]

# Create force and motion instances
force = Force(mass, acceleration)
motion = KinematicMotion([WIDTH // 2, 0], [0, 0], acceleration)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Simulation variables
time = 0
running = True

# Simulation loop
while running:
    dt = clock.tick(FPS) / 1000.0  # seconds
    time += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(WHITE)

    # Get new position
    pos = motion.position(time)
    x, y = int(pos[0]), int(pos[1])

    # Draw object
    pygame.draw.circle(screen, RED, (x, min(y, HEIGHT - 10)), 10)

    # Display info
    pygame.display.flip()

pygame.quit()
sys.exit()
