"""
File: forces.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    This program merges an unknown number of sorted sequences together, keeping them sorted.
"""
sequences = []

# Input is an unknown number of sorted sequences of unknown length.
# Each input sequence is on its own line.
# Input ends with an empty line.
while True:
    integers = input()
    if integers == "":
        break
    integers = [int(_) for _ in integers.split(" ")]
    sequences.append(integers)

sequence = []

for i in range(len(sequences)):
    for j in range(len(sequences[i])):
        sequence.append(sequences[i][j])

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


radix_sort(sequence)

# Output is the sorted sequence that consists of all the input sequences.
print(*sequence)
