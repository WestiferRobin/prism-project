
def print_sector(grid):
    msg = "+"
    for i in range(0, len(grid) * 2 + 1):
        msg += "-"
    msg += "+"
    print(msg)

    for i in range(0, len(grid)):
        msg = "| "
        for j in range(0, len(grid[i])):
            msg += f"{grid[i][j]} "
        msg += "|"
        print(msg)

    msg = "+"
    for i in range(0, len(grid) * 2 + 1):
        msg += "-"
    msg += "+"
    print(msg)
