"""
File: name.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    This program implements the Game of Life.
"""

BOARD_SIZE = 30


def count_alive_neighbours(_grid, _x, _y):
    offsets = [-1, 0, 1]
    _count_neighbours = 0
    # For each offset in x coordinates
    for dx in offsets:
        # For each offset in y coordinates
        for dy in offsets:
            # Checking if the offset for each coordinate is within 0 and board size
            if 0 <= _x + dx < BOARD_SIZE and 0 <= _y + dy < BOARD_SIZE:
                # if the change is not 0
                if dx != 0 or dy != 0:
                    # Modify the grid with the change in offset
                    _count_neighbours += _grid[_x + dx][_y + dy]
    return _count_neighbours


def print_grid(_grid):
    for row in _grid:
        for cell in row:
            print("." if cell == 0 else "*", end="")
        print()


# Creating grid with rows, repeatedly until BOARD_SIZE is reached
grid_now = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
grid_future = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Setting up an example grid
center = BOARD_SIZE // 2
grid_now[center - 1][center] = 1
grid_now[center][center + 1] = 1
grid_now[center + 1][center - 1] = 1
grid_now[center + 1][center] = 1
grid_now[center + 1][center + 1] = 1

print(grid_now)

while input() == "":
    # Check x value in range
    for x in range(BOARD_SIZE):
        # Check y value in range
        for y in range(BOARD_SIZE):
            count_neighbours = count_alive_neighbours(grid_now, x, y)
            if count_neighbours <= 1 or count_neighbours >= 4:
                grid_future[x][y] = 0
            elif count_neighbours == 2:
                grid_future[x][y] = grid_now[x][y]
            elif count_neighbours == 3:
                grid_future[x][y] = 1
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            grid_now[x][y] = grid_future[x][y]

    print_grid(grid_now)
