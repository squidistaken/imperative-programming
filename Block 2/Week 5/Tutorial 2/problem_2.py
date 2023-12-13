# Radius is a positive integer
r = int(input())


# O(n^2)
def count_grid_points(radius):
    count = 0
    x = 0
    # O(n)
    while x <= radius:
        y = 1
        # O(n)
        while y <= radius:
            if x * x + y * y <= radius * radius:
                count += 1
            y += 1
        x += 1

    return 1 + (4 * count)


# O(n)
def new_count_grid_points(radius: int) -> int:
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


print(new_count_grid_points(r))
