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


def count_moves(_maze: list, _y: int, _x: int, _count: int, _max_count: int) -> tuple[int, int]:
    if _maze[_y][_x] == ".":
        _count += 1
    else:
        _max_count = max(_count, _max_count)
        _count = 0

    return _count, _max_count


def get_allowed_moves(_maze: list, _y: int, _x: int, _moves: list[tuple], _visited_points: list[tuple]) -> list[tuple]:
    _possible_moves = []

    for direction in [(_y + 1, _x), (_y - 1, _x), (_y, _x + 1), (_y, _x - 1)]:
        if (direction[0], direction[1]) in _moves and (direction[0], direction[1]) not in _visited_points:
            _possible_moves.append((direction[0], direction[1]))

    return _possible_moves


def move(_maze: list, _y: int, _x: int, _moves: list[tuple], _visited_points: list[tuple], _count: int, _max_count: int):
    _count, _max_count = count_moves(_maze, _y, _x, _count, _max_count)
    _max_count = max(_count, _max_count)
    _visited_points.append((_y, _x))
    _possible_moves = get_allowed_moves(_maze, _y, _x, _moves, _visited_points)

    for i in _possible_moves:
        _y, _x = i
        return move(_maze, _y, _x, _moves, [_[:] for _ in _visited_points], _count, _max_count)

    return _count, _max_count


count, max_count = move(maze, y, x, moves, visited_points, count, max_count)
max_count = max(count, max_count)

print(max_count)
