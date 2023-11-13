"""
File: name.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    Description
"""

# Take in input and convert to a list.
lst = [int(i) for i in input().split(" ")]

bool_lst = []

# the input 1 2 0 represents the path 0 → 1 → 2 → 0.
# Note that this path forms a complete cycle and visits each # of the positions in the list.
initial_num = lst[0] - 1
index = 0


for num in lst:
    if num == initial_num + 1:
        bool_lst.append(True)
    elif num == 0 and num != lst[index - 1]: # and num != lst[initial_num - 1]:
        bool_lst.append(True)
    else:
        bool_lst.append(False)
    initial_num += 1
    index += 1

if all(bool_lst):
    print("Yes")
else:
    print("No")

"""
is [1, 0] a valid sequence? 

does the sequence have to end in 0?

does the sequence have to start with 1?

Input: 1 2 0
Output: Yes

Input: 1 2 2
Output: No

Input: 2 1 0
Output: No
"""
