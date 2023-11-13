"""
File: missingno.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    This program outputs the length of the longest increasing subsequence possible when removing at most
    one value in the original sequence.
"""

# Single line containing an unknown number of integers
lst = [int(_) for _ in input().split(" ")]
seq_lst = []

prev = 0
output = 0

if len(lst) == 1:
    output = 1
else:
    for i in range(len(lst)):
        seq_lst = lst.copy()
        # Removing a number from the list based on the index
        seq_lst.pop(i)
        # We always need to set the count to zero when looking for the next subsequence
        count = 0

        for j in range(len(seq_lst) - 1):
            if seq_lst[j] < seq_lst[j + 1]:
                count += 1
                if count + 1 > output:
                    output = count + 1
            else:
                if count + 1 > output:
                    output = count + 1
                count = 0

# Length of the longest increasing subsequence possible when removing at most one value in the original sequence
print(output)
