"""
File: encoding.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    This program is a simple form of an encoding exercise.
"""

lst_output = []
index = 0

for character in list(input()):
    index += 1
    if character.islower():
        pos = ord(character) - ord("a")
        pos += index
        if pos >= 26:
            pos %= 26
        pos += 97
    elif character.isupper():
        pos = ord(character) - ord("A")
        pos += index
        if pos >= 26:
            pos %= 26
        pos += 65
    else:
        lst_output.append(character)
        continue

    lst_output.append(chr(pos))

print(''.join(lst_output))
