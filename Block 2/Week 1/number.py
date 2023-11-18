"""
File: number.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    This number mimics an arithmetic summation.
"""

# Input for this exercise is a line with three numbers n, m, and k.
n, m, k = map(int, input().split())

if k == 0:
    result = 0
else:
    steps = (m - n)//k
    result = int(n + n*steps + k*((steps*(steps+1))//2))

print(result)
