"""
File: distance.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    This returns the the number of unique pairs (i, j) in a sequence that are exactly k apart.
"""

# First input is the number k
k = int(input())
# Second input is a sequence of integer numbers
integers = [int(_) for _ in input().split(" ")]
integers = list(dict.fromkeys(integers))

MAX_NUMBER = 1000000000
RADIX = 10


def counting_sort(sequence: list[int], factor: int = 1) -> None:
    output = [0] * len(sequence)
    tally = [0] * RADIX
    for value in sequence:
        tally[(value // factor) % RADIX] += 1
    for i in range(1, RADIX):
        tally[i] += tally[i - 1]
    position = len(sequence) - 1
    while position >= 0:
        tally_position = (sequence[position] // factor) % RADIX
        tally[tally_position] -= 1
        output[tally[tally_position]] = sequence[position]
        position -= 1
    for position in range(len(sequence)):
        sequence[position] = output[position]


def radix_sort(sequence: list[int]) -> None:
    factor = 1
    while factor < MAX_NUMBER:
        counting_sort(sequence, factor)
        factor *= RADIX


radix_sort(integers)


count = 0
for i in range(len(integers)):
    for j in range(len(integers)):
        if integers[i] + k == integers[j]:
            count += 1
            break

# Output is the number of unique pairs (i, j) in the sequence that are exactly k apart.
print(count)
