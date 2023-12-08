sequences = []

# Input is an unknown number of sorted sequences of unknown length.
# Each input sequence is on its own line.
# Input ends with an empty line.
while True:
    integers = input()
    if integers == "":
        break
    integers = [int(_) for _ in integers.split(" ")]
    sequences.append(integers)

def check_order(sequence: list[int], n: int):
    if len(sequence) < 3:
        return sequence.append(n)
    for i in range(len(sequence)):
        if sequence[i] < n:
            if sequence[i+1] < n:
                print(True)
                return sequence.insert(i+1, n)

def merge_sorted(sequence: list[list[int]]) -> list[int]:
    new_sequence = []

    for i in range(len(sequence)):
        for j in range(len(sequence[i])):
            check_order(new_sequence, sequence[i][j])




    return new_sequence

final_sequence = merge_sorted(sequences)