"""
File: suitcase.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    This program "packs" a suitcase so that the satisfaction value the owner gets from the items inside
    the suitcase is as high as possible without exceeding the volume of the suitcase
"""

# First line holds two numbers n and v,
# which represent the number n of items that the owner considers packing,
# and the volume v of the suitcase.
n, v = map(int, input().split())
items = {}

# Next n lines each contain a word describing the item, the item’s size, and it’s satisfaction value.
i = 0
while i < n:
    entry = input()
    if entry == "":
        break
    item, item_size, item_satisfaction = entry.split()
    items[item] = (int(item_size), int(item_satisfaction))
    i += 1

# Isolating the dictionary. You could probably ignore this process in another way...
weights = []
satisfactions = []
for j in items:
    weights.append(items[j][0])
    satisfactions.append(items[j][1])


def find_optimal_satisfaction(_v: int, _weights: list[int], _satisfactions: list[int], _n: int):
    # Base case: If there are no items or the volume is zero, then return zero.
    if _n == 0 or _v == 0:
        return 0
    # If the weight of nth item is greater than current taken volume, then this item will not be included in
    # the optimal solution.
    if _weights[_n - 1] > _v:
        return find_optimal_satisfaction(_v, _weights, _satisfactions, _n - 1)
    # Return the maximum between the included item and not included item
    else:
        result = max(_satisfactions[_n - 1] +
                     find_optimal_satisfaction(_v - _weights[_n - 1], _weights, _satisfactions, _n - 1),
                     find_optimal_satisfaction(_v, _weights, _satisfactions, _n - 1))
        return result


print(find_optimal_satisfaction(v, weights, satisfactions, n))
