"""
File: encoding_old_v2.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    This program is a simple form of an encoding exercise.
"""

lst_input = list(input())
alphabet_lowercase = list("abcdefghijklmnopqrstuvwxyz") * (len(lst_input) + 1)
alphabet_uppercase = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") * (len(lst_input) + 1)
lst_output = []

'''
- work out where pos is
- remove ord a
- mod it by 26 (no overflow)
- if >26, subtract by it! think smart not hard
- add a back on

ASCII solution ^^
'''

index = 0

while index < len(lst_input):
    new_pos = index + 1

    # Finds first position of that character
    string_pos = str(lst_input[index])

    if lst_input[index] in alphabet_lowercase:
        current_pos = alphabet_lowercase.index(string_pos)
        lst_output.append(alphabet_lowercase[current_pos + new_pos])
    elif lst_input[index] in alphabet_uppercase:
        current_pos = alphabet_uppercase.index(string_pos)
        lst_output.append(alphabet_uppercase[current_pos + new_pos])
    else:
        lst_output.append(lst_input[index])

    index += 1

print(''.join(lst_output))
