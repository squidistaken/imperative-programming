"""
File: forces.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    Description
"""
sequences = []

# Input is an unknown number of sorted sequences of unknown length.
# Each input sequence is on its own line.
# Input ends with an empty line.
while True:
    integers = input()
    if integers == "":
        break
    sequences.append(integers.split())

# Output is the sorted sequence that consists of all the input sequences.
