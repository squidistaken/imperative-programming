'''
File: name.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    This program is a simple form of encoding exercise.
'''

lst_input = list(input())

'''
Rules:
- Uppercase characters stay uppercase characters, and lowercase characters stay lowercase characters.
- Non-letter characters should not be encoded.
'''

index = 0

while index < len(lst_input):
    # do stuff

lst_output = ''.join(lst_input)

print(lst_output)
