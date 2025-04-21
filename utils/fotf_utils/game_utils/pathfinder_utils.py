import heapq

from configs.game_config import MAP_WIDTH, MAP_HEIGHT


def neighbors(pos):
    x, y = pos
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    return [(x + dx, y + dy) for dx, dy in directions if 0 <= x + dx < MAP_WIDTH and 0 <= y + dy < MAP_HEIGHT]

def heuristic(a, b):
    d_x = abs(a[0] - b[0])
    d_y = abs(a[1] - b[1])
    return (d_x + d_y) + (1.4142 - 2) * min(d_x, d_y)

def a_star(start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}

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