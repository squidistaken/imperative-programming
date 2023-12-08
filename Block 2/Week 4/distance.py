"""
File: distance_old_v1.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    This returns the number of unique pairs (i, j) in a sequence that are exactly k apart.
"""

# First input is the number k
k = int(input())
# Second input is a sequence of integer numbers
integers = [int(_) for _ in input().split(" ")]
integers = list(dict.fromkeys(integers))

count = 0
for i in range(len(integers)):
    for j in range(len(integers)):
        if integers[i] + k == integers[j]:
            count += 1
            break

# Output is the number of unique pairs (i, j) in the sequence that are exactly k apart.
print(count)
