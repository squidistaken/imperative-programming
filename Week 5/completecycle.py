"""
File: completecycle.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    This program checks if a list is a complete cycle via list indices.
"""

lst = [int(_) for _ in input().split(" ")]
cycle = []

i = 0

for n in range(len(lst)):
    cycle.append(lst[i])
    i = lst[i]

# Check any value for each cycle list if there is more than one specific value (ex. more than one 2 values)
if any(cycle.count(x) > 1 for x in cycle):
    print("No")
else:
    print("Yes")
