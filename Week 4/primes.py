"""
File: primes.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    This program checks for the closest prime number below x.
"""

x = int(input())

if x < 2:
    print("Invalid response; x must be greater than 2")
else:
    x -= 1
    while x != 0:
        if (x % 2 == 0) or (x % 3 == 0) or (x % 5 == 0):
            x -= 1
        else:
            print(x)
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
