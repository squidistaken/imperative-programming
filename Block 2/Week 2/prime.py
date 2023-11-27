"""
File: prime.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    This program provides the nth prime. Ex. the 1st prime is 2, 100th prime is 541, etc.
"""

# Input is a number n.
n = int(input())


def find_nth_prime(_n: int) -> int:
    if _n == 1:
        return 2
    num = 1
    count = 1
    # Building the number
    while count < _n:
        num += 2
        if is_prime(num):
            count += 1
    return num


def is_prime(x: int) -> bool:
    if x % 2 == 0:
        return False
    # Odd numbers can be primes, but even numbers cannot.
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True


# Output is the n-th prime in the ordered list of primes
print(find_nth_prime(n))
