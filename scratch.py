lst = [int(_) for _ in input().split(" ")]

def longest_increasing_subsequence(lst):
    n = len(lst)
    if n <= 1:
        return n

    # dp[i] stores the length of the longest increasing subsequence ending at index i
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if lst[i] > lst[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    max_length = max(dp)

    # Now, consider removing at most one element
    for i in range(n):
        for j in range(i+1, n):
            if lst[j] > lst[i]:
                dp[j] = max(dp[j], dp[i] + 1)

    return max(dp)

result = longest_increasing_subsequence(lst)
print(result)