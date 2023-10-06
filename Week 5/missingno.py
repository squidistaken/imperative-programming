"""
File: missingno.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    This program outputs the length of the longest increasing subsequence possible when removing at most
    one value in the original sequence.
"""

lst = [int(_) for _ in input().split(" ")]

prev = 0
count = 0
maximum = 0

for i in range(len(lst)):
    for n in lst:
        if n == i:
            continue
        elif prev < n:
            count += 1
        else:
            count = 0
        maximum = max(maximum, count)
        prev = n

print(maximum)

"""
Input: 1 9 2 3 5 6 7
Output: 6

Input: 1 2 3 3 4 4 5 6 7 8
Output: 6

Input: 1 2 3 4 4 5 6 7 8
Output: 8
"""

"""
prev = 0, cnt = 0, max = 0
for i in range len:
	for n in array:
		idx(n) == i:
			continue
		prev < n:
			cnt += 1
		else:
			cnt = 0
		max = max(max, cnt)
		prev = n;

print(max)
"""
