"""
File: missingno2.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
   This program is an extension to the missingno python assignment, now taking an additional input of numbers allowed
   to remove from the sequence.
"""
# First input contains an unknown number of integers.
integers: list[int] = [int(_) for _ in input().split(" ")]
# Second input is the maximum number k of values you are allowed to remove from this sequence.
k = int(input())

output = 0


def find_longest_subsequence(_subsequence: list[int]):
    global output
    count = 1
    for i in range(len(_subsequence) - 1):
        if _subsequence[i] < _subsequence[i + 1]:
            count += 1
        else:
            output = max(output, count)
            count = 1
        output = max(output, count)


def remove_int(_sequence: list[int], _k: int):
    global integers
    for i in range(len(_sequence)):
        subsequence = _sequence.copy()
        subsequence.pop(i)
        find_longest_subsequence(subsequence)
        if (len(integers) - len(subsequence)) < _k:
            remove_int(subsequence, _k)


remove_int(integers, k)

if k >= len(integers):
    output = 1

print(output)
