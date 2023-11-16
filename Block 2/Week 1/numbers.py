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


# TODO: Find largest possible arithmetic series
def add_nums(start: int, limit: int, step: int) -> int:
    if start >= limit:
        return start
    start += step
    return add_nums(start, limit, step)


# Input for this exercise is a line with three numbers n, m, and k.
n, m, k = map(int, input().split())

# Output is the sum of the numbers from n until m (both inclusive) in steps of size k.
total = add_nums(n, m, k)
print(total)
