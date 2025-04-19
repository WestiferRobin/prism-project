import pygame
from configs.game_config import MAP_HEIGHT, MAP_WIDTH, TILE_HEIGHT, TILE_WIDTH


def generate_tilemap():
    return [["grass" for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]


class FotfGame:
    def __init__(self, name: str = "FotF"):
        pygame.init()
        self.name = name
        self.screen = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h),
                                              pygame.RESIZABLE)
        self.window_width, self.window_height = self.screen.get_size()
        pygame.display.set_caption(name)

        self.clock = pygame.time.Clock()
        self.running = True
        self.camera_offset = [0, 0]
        self.last_move_time = pygame.time.get_ticks()

        self.tilemap = generate_tilemap()
        self.units = [[5, 5]]
        self.selected_units = []
        self.selection_box = None
        self.drag_start = None
        self.unit_targets = {}

    def iso_coords(self, x, y):
        map_pixel_width = (MAP_WIDTH + MAP_HEIGHT) * TILE_WIDTH // 2
        map_pixel_height = (MAP_WIDTH + MAP_HEIGHT) * TILE_HEIGHT // 2
        offset_x = (self.window_width - map_pixel_width) // 2 + self.camera_offset[0]
        offset_y = (self.window_height - map_pixel_height) // 2 + self.camera_offset[1]
        screen_x = (x - y) * TILE_WIDTH // 2 + offset_x + map_pixel_width // 2
        screen_y = (x + y) * TILE_HEIGHT // 2 + offset_y
        return screen_x, screen_y

    def screen_to_tile(self, screen_x, screen_y):
        map_pixel_width = (MAP_WIDTH + MAP_HEIGHT) * TILE_WIDTH // 2
        map_pixel_height = (MAP_WIDTH + MAP_HEIGHT) * TILE_HEIGHT // 2
        offset_x = (self.window_width - map_pixel_width) // 2 + self.camera_offset[0]
        offset_y = (self.window_height - map_pixel_height) // 2 + self.camera_offset[1]
        offset_x += map_pixel_width // 2  # align with iso_coords()
        temp_x = screen_x - offset_x
        temp_y = screen_y - offset_y
        tile_x = ((temp_y / (TILE_HEIGHT / 2)) + (temp_x / (TILE_WIDTH / 2))) / 2
        tile_y = ((temp_y / (TILE_HEIGHT / 2)) - (temp_x / (TILE_WIDTH / 2))) / 2
        return int(tile_x), int(tile_y)

    def handle_mouse_events(self, event):
        # DEBUG: log where you're clicking and what tile it's being interpreted as
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            tile_x, tile_y = self.screen_to_tile(mouse_x, mouse_y)
            print(f"[DEBUG] Click at ({mouse_x}, {mouse_y}) → Tile: ({tile_x}, {tile_y})")
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                tile_x, tile_y = self.screen_to_tile(mouse_x, mouse_y)
                tile_x = max(0, min(MAP_WIDTH - 1, tile_x))
                tile_y = max(0, min(MAP_HEIGHT - 1, tile_y))
                for unit in self.units:
                    if unit[0] == tile_x and unit[1] == tile_y:
                        self.selected_units = [unit]
                        return
                if self.selected_units:
                    for unit in self.selected_units:
                        self.unit_targets[tuple(unit)] = [tile_x, tile_y]
                else:
                    self.drag_start = pygame.mouse.get_pos()
                    self.selection_box = pygame.Rect(*self.drag_start, 0, 0)

            elif event.button == 3:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                tile_x, tile_y = self.screen_to_tile(mouse_x, mouse_y)
                tile_x = max(0, min(MAP_WIDTH - 1, tile_x))
                tile_y = max(0, min(MAP_HEIGHT - 1, tile_y))
                for unit in self.units:
                    if unit[0] == tile_x and unit[1] == tile_y:
                        return  # Don't deselect if right-clicked on unit
                self.selected_units.clear()
        elif event.type == pygame.MOUSEMOTION and self.drag_start:
            current = pygame.mouse.get_pos()
            x, y = self.drag_start
            self.selection_box.update(x, y, current[0] - x, current[1] - y)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.selection_box:
                self.selected_units.clear()
                for unit in self.units:
                    screen_x, screen_y = self.iso_coords(*unit)
                    unit_rect = pygame.Rect(screen_x, screen_y, TILE_WIDTH, TILE_HEIGHT)
                    if self.selection_box.colliderect(unit_rect):
                        self.selected_units.append(unit)
                self.selection_box = None
                self.drag_start = None

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
            else:
                self.handle_mouse_events(event)

        keys = pygame.key.get_pressed()
        cam_speed = 20
        if keys[pygame.K_w]: self.camera_offset[1] += cam_speed
        if keys[pygame.K_s]: self.camera_offset[1] -= cam_speed
        if keys[pygame.K_a]: self.camera_offset[0] += cam_speed
        if keys[pygame.K_d]: self.camera_offset[0] -= cam_speed

    def update(self):
        new_unit_targets = {}
        move_speed = 0.125  # Villager-like smooth speed

        def neighbors(pos):
            x, y = pos
            steps = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
            result = []
            for dx, dy in steps:
                nx, ny = x + dx, y + dy
                if 0 <= nx < MAP_WIDTH and 0 <= ny < MAP_HEIGHT:
                    result.append((nx, ny))
            return result

        def a_star(start, goal):
            import heapq
            open_set = []
            heapq.heappush(open_set, (0, start))
            came_from = {}
            g_score = {start: 0}

            def heuristic(a, b):
                dx = abs(a[0] - b[0])
                dy = abs(a[1] - b[1])
                return (dx + dy) + (1.4142 - 2) * min(dx, dy)  # Octile distance  # Manhattan distance

            while open_set:
                _, current = heapq.heappop(open_set)
                if current == goal:
                    break
                for neighbor in neighbors(current):
                    dx = abs(neighbor[0] - current[0])
                    dy = abs(neighbor[1] - current[1])
                    step_cost = 1.4142 if dx == 1 and dy == 1 else 1
                    tentative_g = g_score[current] + step_cost
                    if neighbor not in g_score or tentative_g < g_score[neighbor]:
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g
                        f = tentative_g + heuristic(neighbor, goal)
                        heapq.heappush(open_set, (f, neighbor))

            path = []
            node = goal
            while node in came_from:
                path.append(node)
                node = came_from[node]
            path.append(start)
            return path[::-1]

        for unit in self.units:
            unit_key = tuple(unit)
            if unit_key in self.unit_targets:
                target = tuple(self.unit_targets[unit_key])
                start = (int(unit[0]), int(unit[1]))
                path = a_star(start, target)
                if len(path) > 1:
                    next_step = path[1]
                    dx = next_step[0] - unit[0]
                    dy = next_step[1] - unit[1]
                    dist = (dx ** 2 + dy ** 2) ** 0.5
                    if dist < 0.01:
                        unit[0], unit[1] = round(next_step[0]), round(next_step[1])
                    else:
                        unit[0] += (dx / dist) * move_speed
                        unit[1] += (dy / dist) * move_speed
                    new_unit_targets[tuple(unit)] = list(target)
                else:
                    unit[0], unit[1] = round(target[0]), round(target[1])
        self.unit_targets = new_unit_targets

    def draw_grid(self):
        target_tiles = set(tuple(v) for v in self.unit_targets.values())
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                screen_pos = self.iso_coords(x, y)
                color = (255, 255, 0) if (x, y) in target_tiles else (34, 139, 34)
                points = [
                    (screen_pos[0], screen_pos[1] + TILE_HEIGHT // 2),
                    (screen_pos[0] + TILE_WIDTH // 2, screen_pos[1]),
                    (screen_pos[0] + TILE_WIDTH, screen_pos[1] + TILE_HEIGHT // 2),
                    (screen_pos[0] + TILE_WIDTH // 2, screen_pos[1] + TILE_HEIGHT),
                ]
                pygame.draw.polygon(self.screen, color, points)
                pygame.draw.polygon(self.screen, (50, 50, 50), points, 1)

    def draw_units(self):
        for unit in self.units:
            x, y = unit
            screen_x, screen_y = self.iso_coords(x, y)
            center_x = screen_x + TILE_WIDTH // 2
            center_y = screen_y + TILE_HEIGHT // 2
            pygame.draw.circle(self.screen, (0, 200, 255), (center_x, center_y), 10)
            if unit in self.selected_units:
                pygame.draw.circle(self.screen, (255, 255, 0), (center_x, center_y), 14, 2)

    def draw(self):
        self.screen.fill((0, 0, 0))

        self.draw_grid()
        self.draw_units()
        if self.selection_box:
            pygame.draw.rect(self.screen, (0, 255, 255), self.selection_box, 1)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
        print(f"Exiting {self.name} Game")
        pygame.quit()


def run_fotf():
    FotfGame().run()
