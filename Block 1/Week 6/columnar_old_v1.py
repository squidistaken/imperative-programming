"""
File: columnar_old_v1.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    Description
"""

from math import ceil

text = list(input())
column_order = input()

encoded_text = []
pos = 0

jump = ceil(len(text) / len(column_order))
print(jump)

for i in range(len(column_order) - 1):
    pos = 0 + i
    while pos < len(text):
        encoded_text.append(text[pos])
        pos += jump

print(''.join(encoded_text))

"""
Idea:

Get the length of the column, divide it by the length of the string?

Create a 2D array with the length of the column * height?

Build string based on the values in the indices.
"""

"""
Input: A line of plain text. 
       5726341
Output: i.l tnlxeatAonipe f

Input: It was the best of times, it was the worst of times.
       243156
Output: we mttr .I e ,a m htii ofsttst swoea oe hstsbfsweti

Input: Make sure your output ends with the newline character (\n).
       312
Output: a ryruuesi eei acr\.kseo ttn tt wncrt nMeu uop dwhhnlehae()
"""
