"""
File: mazerunner_old_v1.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    Description
"""

"""
Intended Approach:
max = 0

- Check for all possible movements [( , )]
- For all directions, check if there is a "."
- Temporarily replace . with an empty square, define new pos, recursive call the check function again
- Once moved, add back the dot.

Return of the recursive call: max += 1

"""



def move(_maze, _y, _x) -> int:
    # Down, Up, Right, Left
    directions = [(_y + 1, _x), (_y - 1, _x), (_y, _x + 1), (_y, _x - 1)]
    global count

    for direction in directions:
        if (direction[0], direction[1]) in visited:
            continue
        if _maze[direction[0]][direction[1]] == "#":
            continue
        elif _maze[direction[0]][direction[1]] == ".":
            count += 1
            new_y, new_x = direction[0], direction[1]
            visited.append((_y, _x))
        # elif _maze[direction[0]][direction[1]] == " ":
            # return count
        else:
            return count

        return move(_maze, new_y, new_x)


def get_start_pos(_maze: list) -> tuple:
    start_pos = []
    for _y in range(len(_maze)):
        row = _maze[_y]
        for _x in range(len(row)):
            if _maze[_y][_x] == "@":
                start_pos.append(_y)
                start_pos.append(_x)

    return tuple(start_pos)


# Building 2D Array
maze = []
while True:
    maze_points = input()
    if maze_points == "":
        break
    else:
        maze.append(list(list(maze_points)))

visited = [(0, 0)]
count = 0

y, x = get_start_pos(maze)

maximum = move(maze, y, x)

print(maximum)

"""
Input:
#######
#.... #
##@##.#
# ....#
#######

Output: 5

Input:
#########
#@#...#.#
#.#.#.#.#
#...#...#
#########

Output: 14

Input:
#########
#.#...#.#
#.#.#@#.#
#...#...#
#########

Output: 9
"""
