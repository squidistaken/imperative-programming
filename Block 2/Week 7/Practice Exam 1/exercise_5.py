# O(N)
def fibonacci_index(n: int) -> int:
    """
    Returns the largest index of the Fibonacci sequence that
    does not exceed n. The Fibonacci sequence is defined by
    F(0) = 0, F(1) = 1, F(m) = F(m - 1) + F(m - 2)
    :param n: upper limit of the Fibonacci number
    :return: max(i) so that F(i) <= n
    """
    if (n <= 1):
        return n
    
    prev, next = 1, 1
    index = 1

    while next <= n:
        prev, next = next, next + prev
        index += 1

    return index
