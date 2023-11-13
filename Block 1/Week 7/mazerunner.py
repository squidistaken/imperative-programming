maze = []
count = 0
max_count = 0
visited_points = []

# Input consists of an unknown number of lines, ending with an empty line.
while True:
    maze_points = input()

    if maze_points == "":
        break
    else:
        maze.append(list(list(maze_points)))


# Defining where our start position "@" is.
def get_start_pos(_maze: list) -> tuple:
    start_pos = ()

    for _y in range(len(_maze)):
        row = _maze[_y]
        for _x in range(len(row)):
            if _maze[_y][_x] == "@":
                start_pos = (_y, _x)

    return start_pos


# Defining where all possible moves to "." are.
def get_moves(_maze: list) -> list[tuple]:
    _moves = []

    for _y in range(len(_maze)):
        row = _maze[_y]
        for _x in range(len(row)):
            if _maze[_y][_x] == ".":
                _moves.append((_y, _x))

    return _moves


y, x = get_start_pos(maze)
moves = get_moves(maze)


def count_moves(_maze: list, _y: int, _x: int):
    global count
    global max_count

    if _maze[_y][_x] == ".":
        count += 1
    else:
        max_count = max(count, max_count)
        count = 0


def get_allowed_moves(_maze: list, _y: int, _x: int, _visited_points: list[tuple]) -> list[tuple]:
    global moves
    _possible_moves = []

    for direction in [(_y + 1, _x), (_y - 1, _x), (_y, _x + 1), (_y, _x - 1)]:
        if (direction[0], direction[1]) in moves and (direction[0], direction[1]) not in _visited_points:
            _possible_moves.append((direction[0], direction[1]))

    return _possible_moves


def move(_maze: list, _y: int, _x: int, _visited_points: list[tuple]):
    global count
    global max_count

    count_moves(_maze, _y, _x)

    max_count = max(count, max_count)

    _visited_points.append((_y, _x))
    _possible_moves = get_allowed_moves(_maze, _y, _x, _visited_points)
    store_count = count

    if len(_possible_moves) > 1:
        for i in range(len(_possible_moves)):
            count = store_count
            _y, _x = _possible_moves[i]
            move(_maze, _y, _x, [_[:] for _ in _visited_points])
    elif len(_possible_moves) != 0:
        _y, _x = _possible_moves[0]
        move(_maze, _y, _x, _visited_points)


move(maze, y, x, visited_points)
max_count = max(count, max_count)

print(max_count)
