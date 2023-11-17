"""
File: name.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    Description
"""

"""
Outline:
- 
"""

# Input for this exercise is a line with three numbers n, m, and k.
n, m, k = map(int, input().split())

total = 0

# TODO: Find largest possible arithmetic series
def add_nums(start: int, limit: int, step: int) -> int:
    global total
    if start >= limit:
        start = total
        return start
    total += start
    start += step
    return add_nums(start, limit, step)

# Output is the sum of the numbers from n until m (both inclusive) in steps of size k.
total = add_nums(n, m, k)

print(total)
