'''
File: detection.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    This program is a basic hit detection for a rectangular object.
'''

# Coordinates of a rectangle
x = int(input("x: "))
y = int(input("y: "))
w = int(input("w: "))
z = int(input("z: "))

# Coordinates of a point
a = int(input("a: "))
b = int(input("b: "))

# Sorting min and max coordinates
x_min, x_max = min(x, w), max(x, w)
y_min, y_max = min(y, z), max(y, z)

if ((a == x or a == w) or (b == y or b == z)) and ((x_min < a < x_max) or (y_min < b < y_max)):
    print("EDGE")
elif (x_min < a < x_max) and (y_min < b < y_max):
    print("INSIDE")
else:
    print("OUTSIDE")
