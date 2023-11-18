# A naive recursive implementation
# of 0-1 Knapsack Problem

# Returns the maximum value that
# can be put in a knapsack of
# capacity W


def find_optimal_satisfactions(_v, _weights, _satisfactions, _n):
    # Base Case
    if _n == 0 or _v == 0:
        return 0

    # If weight of the nth item is
    # more than Knapsack of capacity W,
    # then this item cannot be included
    # in the optimal solution
    if _weights[_n - 1] > _v:
        return find_optimal_satisfactions(_v, _weights, _satisfactions, _n - 1)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(_satisfactions[_n - 1] +
                   find_optimal_satisfactions(_v - _weights[_n - 1], _weights, _satisfactions, _n - 1),
                   find_optimal_satisfactions(_v, _weights, _satisfactions, _n - 1))


# end of function knapSack


# Driver Code
if __name__ == '__main__':
    profit = [10, 100, 95]
    weight = [50, 51, 50]
    W = 100
    n = len(profit)
    print(find_optimal_satisfactions(W, weight, profit, n))

# This code is contributed by Nikhil Kumar Singh
