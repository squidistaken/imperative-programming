"""
File: missing.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    This program checks for a missing number in an arithmetic sequence.
"""


# TODO: Optimise
def find_missing(sequence: list[int]) -> tuple[int, int]:
    step = (sequence[-1] - sequence[0]) // len(sequence)
    for i in enumerate(range(sequence[0], sequence[-1], step)):
        if i[1] not in sequence:
            return i[0], i[1]
