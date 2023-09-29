"""
File: encoding_old.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    This program is a simple form of an encoding exercise. Does not work!
"""

"""
Rules:
- Uppercase characters stay uppercase characters, and lowercase characters stay lowercase characters.
- Non-letter characters should not be encoded.
"""

#
lst_input = list(input())
lst_output = []

index = 0

# 33 = !
# 46 = .
# 63 = ?
# 32 =  (the space)

# 65-90 = A-Z
# 97-122 = a-z
while index < len(lst_input):
    lst_index_unicode = ord(lst_input[index])
    # if char_unicode == range(65, 90) or range(97, 122) or 36 or 46 or 63:
    print(lst_index_unicode)
    lst_index_unicode += index + 1

    print(lst_index_unicode)
    '''
    
    
    if 65 > lst_index_unicode < 97:
        print("Invalid; no non-letter characters should be encoded.")
        break
    else:
        lst_index_unicode += index + 1

        # TODO: figure out the rest :(

        
        if lst_index_unicode > 122:
            lst_index_unicode -= 27 (ex. z -> ? -> a)
            lst_index_unicode += index + 1
        else:
            lst_index_unicode += index + 1
        
    index += 1
    '''

    lst_output.append(chr(lst_index_unicode))
    index += 1

print(''.join(lst_output))

'''
Input: abcdefghijklmnopqrstuvwxyz
Output: bdfhjlnprtvxzbdfhjlnprtvxz

Input: Hello World!
Output: Igopt Dwavo!

Input: What's in a name? That which we call a rose...
Output: Xjdx'y qw l aobu? Mbvp ugidj aj jiuv m fdiv...
'''
