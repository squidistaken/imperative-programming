"""
File: disc.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    Description
"""
# Input is a single integer number r, which represents the radius of a disc with center (0, 0).
r = int(input())

# TODO: Optimise to O(nlog(n))?
def count_grid_points(radius: int) -> int:
    count = 0
    x, y = radius, radius
    # O(n)
    while x >= 0:
        if y == 0:
            break
        if x * x + y * y <= radius * radius:
            count += 1
        if x == 0:
            x = radius
            y -= 1
        x -= 1

    return 1 + (4 * count)


# Output is the number of integer grid points that are contained within this disc (including the edge).
print(count_grid_points(r))
