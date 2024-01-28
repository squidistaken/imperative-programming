# This will not compile on purpose!
def merge(sequence = list[int], midpoint = int) -> list[int]:
    left = 0
    right = midpoint
    mergedList = [0] * len(sequence)
    # range(len(mergedList))
    for position in range(mergedList):
        if left < midpoint:
            ## && -> and
            if right < len(sequence) && sequence[left] > sequence[right]:
                mergedList[position] = sequence[right]
                # += 1
                right -= 1
            else:
                mergedList[position] = sequence[left]
                left += 1
        # Else case needed
    # Return mergedList
    return sequence
