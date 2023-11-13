"""
File: missingno_old_v1.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    This program outputs the length of the longest increasing subsequence possible when removing at most
    one value in the original sequence.
"""

# Single line containing an unknown number of integers
lst = [int(_) for _ in input().split(" ")]

prev = 0
count = 0
output = 0

for i in range(len(lst)):
    is_not_i = False
    for n in lst:
        # If the lst index of i is equal to n
        if lst[i] == n:
            # "Removing" the number from the list
            if is_not_i:
                count += 1
            else:
                is_not_i = True
                continue
        # Comparing previous with new value
        elif n > prev:
            count += 1
        else:
            count = 1
        # output = max(output, count)
        prev = n
        output = max(output, count)

# Length of the longest increasing subsequence possible when removing at most one value in the original sequence
print(output)

"""
Input: 1 9 2 3 5 6 7
Output: 6

Input: 1 2 3 3 4 4 5 6 7 8
Output: 6

Input: 1 2 3 4 4 5 6 7 8
Output: 8
"""