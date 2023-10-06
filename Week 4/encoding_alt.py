line_to_encode = input()
offset = 1
encoded_line = ""
for char in line_to_encode:
    if "a" <= char <= "z":
        encoded_line += chr(((ord(char) - ord("a") + offset) % 26) + ord("a"))
    elif "A" <= char <= "Z":
        encoded_line += chr(((ord(char) - ord("A") + offset) % 26) + ord("A"))
    else:
        encoded_line += char
    offset += 1
print(encoded_line)