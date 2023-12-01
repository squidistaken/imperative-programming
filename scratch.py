def missingElementAP(arr, n):
    # Common Difference
    d = (arr[-1] - arr[0]) // len(arr)
    low = 0
    high = len(arr) - 1
    while low < high:
        # Finding the middle index
        mid = int(low + (high - low) / 2)

        # if mid and the immediate next element to mid are not in AP, then missing element is arr[mid] + d.
        if arr[mid + 1] - arr[mid] != d:
            return arr[mid] + d

        # if mid and the immediate previous element to mid are not in AP, then missing element is arr[mid-1] + d.
        if mid > 0 and arr[mid] - arr[mid - 1] != d:
            return arr[mid - 1] + d

        # if elements of the left half are in AP, then the missing element is in the right half.
        if arr[mid] == arr[0] + mid * d:
            low = mid + 1

        # else the missing element is in the left half.
        else:
            high = mid - 1
    return "invalid"

print(missingElementAP([4, 7, 10, 16, 19], 5))