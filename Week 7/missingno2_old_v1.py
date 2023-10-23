"""
File: missingno2_old_v1.py
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
            count = 0
        output = max(output, count)


# TODO: Recursion takes too long for some cases
def remove_int(_sequence: list[int], _k: int):
    global integers
    for i in range(len(_sequence) - 1):
        if _sequence[i - 1] < _sequence[i] < _sequence[i + 1]:
            continue
        item = _sequence.pop(i)

        find_longest_subsequence(_sequence)
        if len(integers) - len(_sequence) < _k:
            remove_int(_sequence, _k)
        _sequence.insert(i, item)


remove_int(integers, k)

if k >= len(integers):
    output = 0

# Output is the length of the longest increasing subsequence possible when removing at most k values from the
# original sequence
print(output)

"""
Input:
1 9 2 3 5 7 6 8
2
Output:
6

Input:
1 2 3 3 4 4 5 6 7 8
1
Output:
6

Input:
1 2 3 3 4 4 5 6 7 8
2
Output:
8
"""
