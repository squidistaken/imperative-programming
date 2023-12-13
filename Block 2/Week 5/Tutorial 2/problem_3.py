N = int(input())

grid = []
# O(n)
while len(grid) < N:
    grid.append([int(_) for _ in input().split(" ")])

# O(n^3)
for i in range(N):
    for j in range(N):
        for k in range(N):
            pass
        pass
    pass
