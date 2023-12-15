"""
File: disc.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    This program counts all possible grid points in a circle with r radius.
"""
# Input is a single integer number r, which represents the radius of a disc with center (0, 0).
r = int(input())


def count_grid_points(radius: int) -> int:
    axis_count = 1 + 4 * radius
    count = 0
    x = 1
    y = radius

    while x <= radius:
        if (x * x + y * y) > radius * radius:
            y -= 1
        else:
            count += y
            x += 1

    return (count * 4) + (1 + (4 * radius))


# Output is the number of integer grid points that are contained within this disc (including the edge).
print(count_grid_points(r))
