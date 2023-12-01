# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1
"""def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1


# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 40

# Function call
result = binary_search(arr, x)"""


def find_missing(sequence: list[int], prev: int = 0) -> tuple[int, int]:
    low = sequence[0]
    high = sequence[-1]
    mid_value = (high + low) // 2
    mid_index = len(sequence) // 2
    new_sequence = sequence
    pos = 0

    # TODO: This in a while loop
    while low < high:
        if mid_value > new_sequence[mid_index]:
            new_sequence = new_sequence[mid_index:]

        else:
            new_sequence = new_sequence[:mid_index]
        pos += sequence.index(new_sequence[0])
        low = mid_value
        mid_value = (high + low) // 2
        mid_index = len(sequence) // 2


"""    low = sequence[0]
    high = sequence[-1]

    mid_value = (high + low) // 2
    mid_index = len(sequence) // 2

    step = (high - low) // len(sequence)
    # Upper half has the missing number
    if mid_value > sequence[mid_index]:
        return find_missing(sequence[mid_index:])
    # Lower half has the missing number
    if mid_value < sequence[mid_index]:
        return find_missing(sequence[:mid_index])"""


print(find_missing([4, 7, 10, 16, 19]))