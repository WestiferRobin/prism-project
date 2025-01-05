
def build_sector(m, n):
    grid = []
    for i in range(0, m):
        line = []
        for j in range(0, n):
            line.append('~')
        grid.append(line)
    return grid
