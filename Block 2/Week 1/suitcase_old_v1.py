"""
File: suitcase_old_v1.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    Description
"""

# First line holds two numbers n and v,
# which represent the number n of items that the owner considers packing,
# and the volume v of the suitcase.
n, v = map(int, input().split())
items = {}
i = 0
# Next n lines each contain a word describing the item, the item’s size, and it’s satisfaction value.
while i < n:
    entry = input()
    if entry == "":
        break
    item, item_size, item_satisfaction = entry.split()
    items[item] = (int(item_size), int(item_satisfaction))
    i += 1


def find_optimal_satisfaction(_items: dict, _v: int, _item_satisfaction: int = 0) -> int:
    for j in _items:
        if 0 < _items[j][0] <= _v:
            _v -= _items[j][0]
            _item_satisfaction += _items[j][1]
            _items.pop(j)
            return find_optimal_satisfaction(_items, _v, _item_satisfaction)
        else:
            continue
    return _item_satisfaction


# Output should be the optimal satisfaction value that can be achieved from
# a set of items that fit inside the suitcase.
print(find_optimal_satisfaction(items, v))

# for each item, consider to take or dont
# Best way to do it: keep track of index/pos and total volume
# score = recursive call to next parameter
# if current item can still fit, take a maximum between the score and taking the item (recursive call)
# dont modify the dictionary, keep track of the index