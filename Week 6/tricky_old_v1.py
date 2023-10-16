"""
File: tricky_old_v1.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    Description
"""


def count_tricky_squares(_a, _b):
    count = 0
    for i in range(_a, _b + 1):
        temp_lst = list(str(i))
        j = 0
        while j * j <= i:
            if j * j == i and any(temp_lst.count(x) > 1 for x in temp_lst):
                count += 1
            j += 1
    return count


# Input consists of a line with two numbers a and b with 1 ≤ a < b ≤ 1010
num = [int(_) for _ in input().split(" ")]

a = num[0]
b = num[1]

# Output is the number of tricky squares that are at least a and at most b
print(count_tricky_squares(a, b))

"""
Input: 1 100
Output: 1

Input: 100 225
Output: 4

Input: 12345 123456
Output: 130 - Times out timewise
"""
