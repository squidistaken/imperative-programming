"""
File: name.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    Description
"""

x = int(input())
flag = False


if x < 2:
    print("Invalid response; x must be greater than 2")
else:
    x -= 1
    while not flag:
        print(x)
        # TODO: Tweak the conditional!
        if (x % 2 == 0) or (x % 3 == 0) or (x % 5 == 0) or (x % 31 == 0) or (x % 41 == 0) or (x % 109 == 0) or (x % 11 == 0) or (x % 53 == 0):
            x -= 1
        else:
            print(x)
            flag = True
            break


"""
Input:  1234
Output: 1231

Input:  11
Output: 7

- todo
Input:  123456789
Output: 123456761
"""
