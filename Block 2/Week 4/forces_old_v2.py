"""
File: forces_old_v2.py
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


def get_position(sequence: list[int], n: int) -> int:
    pos = 0

    for i in range(len(sequence)):
        if n > sequence[i]:
            pos += 1
    return pos


def merge_sorted(sequence: list[list[int]]) -> list[int]:
    new_sequence = max(sequence, key=len)
    sequence.pop(sequence.index(max(sequence, key=len)))

    for i in range(len(sequence)):
        for j in range(len(sequence[i])):
            new_sequence.insert(get_position(new_sequence, sequence[i][j]), sequence[i][j])

    return new_sequence


final_sequence = merge_sorted(sequences)

print(*final_sequence)
