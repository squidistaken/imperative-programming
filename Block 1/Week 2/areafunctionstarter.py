'''
File: area.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    This program imports functions from area.py, and uses them to get the area of rectangles and triangles.
'''

# Imports everything from area
from area import *

shape_input = str(input())
base = float(input())
height = float(input())

match shape_input:
    case "triangle":
        print(get_area_of_triangle(base, height))
    case "rectangle":
        print(get_area_of_rectangle(base, height))
    case other:
        print("Shape not found.")