"""
File: disc.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    Description
"""
# Input is a single integer number r, which represents the radius of a disc with center (0, 0).
r = int(input())

# Horizontal and vertical "lines"
points = 1 + (4 * r)

adj = 1

# TODO: Example 3 works but 1+2 do not
while adj <= r:
    diff = ((((r ** 2) + (adj ** 2)) ** 0.5) - r)
    if adj == r:
        diff = (((r ** 2) + (adj ** 2)) ** 0.5)
        points += 4 * round(diff)
    else:
        points += 4 * ((r - 1) * round(diff))
    adj += 1

# Output is the number of integer grid points that are contained within this disc (including the edge).
print(points)
