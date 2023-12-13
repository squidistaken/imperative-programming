from random import randrange

# N is a positive integer (i.e. N > 0).
N = randrange(1, 1000)


# Time Complexity: O(nlog(n))
def time_complexity_1():
    s = 0
    # O(n)
    for i in range(0, N, 3):
        j = 3 * N
        # O(log(n))
        while j > 0:
            j /= 2
            s += i * j


# Time Complexity: O(log(n))
def time_complexity_2():
    s = 0
    i = 1
    while i < N * N:
        s += i * i
        i *= 3


# Time Complexity: O(sqrt(n))
def time_complexity_3():
    i = 0
    s = 0
    # O(n^2)
    while s < N:
        s += i
        i += 1
    # O(n)
    while i > 0:
        s += i
        i -= 1


# Time Complexity: O(n^2)
def time_complexity_4():
    j = 0
    s = 0
    # O(n)
    for i in range(N):
        # O(n)
        for j in range(0, 5 * i, 2):
            s += i + j


# Time Complexity: O(nlog(n))
def time_complexity_5():
    s = 0
    # O(n)
    for i in range(N, 0, -1):
        d = 2 + i % 5
        j = 1
        # O(nlog(n)
        while j < N:
            s += j * s
            j *= d


# Time Complexity: O(n^2)
def time_complexity_6():
    s = 0
    i = 0
    # O(n^2)
    while s < N * N:
        s += i
        i += 1
