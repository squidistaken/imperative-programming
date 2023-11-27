"""
File: cards.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    This exercise finds all the possible combinations of distinct cards (d) you can have in a hand (h).
"""

# Input is the number of cards h in a hand and the number d of distinct labels.
# Input is how many cards exist for each label.
h, d = map(int, input().split())
d_count = list(map(int, input().split()))
index = d - 1


def find_distinct_hands(size, cards_per_label, current_index) -> int:
    # Case for checking when you have no more cards left to fill up your hand.
    if current_index == 0:
        # If you run out of a specific type of card, 0 is returned. Else, 1 is returned.
        return 1 if cards_per_label[0] >= size else 0

    total = 0

    # Cycling through each card label type and setting up combinations via for loop.
    for i in range(cards_per_label[current_index] + 1):
        # Optimisation: If you have more cards to take than what you can hold, why bother taking the rest? Break.
        if i > size:
            break
        total += find_distinct_hands(size - i, cards_per_label, current_index - 1)

    return total


# Output is the number of distinct hands of size h that are possible given the description.
print(find_distinct_hands(h, d_count, index))
