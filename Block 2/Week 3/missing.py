"""
File: missing.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    This program checks for a missing number in an arithmetic sequence.
"""


# "Replicating" binary search
def find_missing(sequence: list[int]) -> tuple[int, int]:
    diff = (sequence[-1] - sequence[0]) // len(sequence)
    low = 0
    high = len(sequence) - 1
    # Allow for constant iteration
    while low < high:
        # Midpoint position
        mid = low + (high - low) // 2
        # If the arithmetic progression is not actually equal to the real arithmetic progression, we can return
        if sequence[mid + 1] - sequence[mid] != diff:
            return mid + 1, sequence[mid] + diff
        # Same condition, but assuming the midpoint is different.
        if mid > 0 and sequence[mid] - sequence[mid - 1] != diff:
            return mid, sequence[mid - 1] + diff
        # If all elements are in the left, then the certain element is on the right side
        if sequence[mid] == sequence[0] + mid * diff:
            low = mid + 1
        # Otherwise the element is on the left side
        else:
            high = mid - 1
