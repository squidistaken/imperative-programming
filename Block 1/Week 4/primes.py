"""
File: primes.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    This program checks for the closest prime number below x.
"""
from math import sqrt


def is_prime(x):
    # Loops for each n in a range from 2 to the square root of x + 1
    for n in range(2, int(sqrt(x) + 1)):
        # if the modulus of x and n results in zero, return false and reduce x
        if x % n == 0:
            return False
    return True


x = int(input()) - 1

if x < 2:
    print("Invalid response; x must be greater than 2")
else:
    while not is_prime(x):
        x -= 1
    else:
        print(x)
