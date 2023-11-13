"""
File: tricky.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    This program locates for tricky numbers (Numbers with ONE duplicate ints) within range a to b.
"""
from math import sqrt, ceil


def check_duplicates(_x):
    lst_duplicates = [0] * 10
    duplicate_num = 0

    for i in str(_x):
        lst_duplicates[int(i)] += 1
    for j in lst_duplicates:
        if j > 1:
            duplicate_num += 1
    if duplicate_num == 1:
        return True
    return False


# Input consists of a line with two numbers a and b with 1 ≤ a < b ≤ 10^10
num = [int(_) for _ in input().split(" ")]

a = ceil(sqrt(num[0]))
b = ceil(sqrt(num[1]))
tricky_squares = 0

# Our real range is squares, since this problem only attacks that.
squares = [_ ** 2 for _ in range(a, b + 1)]

for square in squares:
    tricky_squares += check_duplicates(square)

# Output is the number of tricky squares that are at least a and at most b
print(tricky_squares)
