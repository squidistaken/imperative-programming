"""
File: road.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    Description
"""

# The input is a line with the number of villages N
N = int(input())
#
n = 0

# The input are the (positive and integer) lengths of the direct roads between villages, so the i-th number on
# j-th line represents the length of the direct road between villages i and j.
grid = []
while n < N:
    grid.append([int(_) for _ in input().split(" ")])
    n += 1

# Output is N lines that represent the shortest distance between each of the villages.
