"""
File: road.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    This program finds the shortest distance between any pair of villages among N villages.
"""

# The input is a line with the number of villages N
N = int(input())

# The input are the (positive and integer) lengths of the direct roads between villages, so the i-th number on
# j-th line represents the length of the direct road between villages i and j.
grid = []
while len(grid) < N:
    grid.append([int(_) for _ in input().split(" ")])


# Floyd-Warshall's Algorithm
def find_shortest_distances(matrix: list[list[int]]) -> list[list[int]]:
    new_grid = matrix
    length = len(new_grid)

    for k in range(length):
        for i in range(length):
            for j in range(length):
                # Don't update state if i and j are the same.
                if i == j:
                    continue
                # Zero = Impossible to reach
                if ((new_grid[i][j] == 0 or new_grid[i][j] > new_grid[i][k] + new_grid[k][j])
                        and new_grid[i][k] != 0 and new_grid[k][j] != 0):
                    new_grid[i][j] = new_grid[i][k] + new_grid[k][j]
                    new_grid[j][i] = new_grid[i][k] + new_grid[k][j]

    return new_grid


# Output is N lines that represent the shortest distance between each of the villages.
for row in find_shortest_distances(grid):
    print(*row)
