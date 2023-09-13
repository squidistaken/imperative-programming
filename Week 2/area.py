'''
File: area.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    This program calculates the area of a triangle or rectangle, depending on what is specified.
'''


def get_area_of_triangle(b, h):
    area = (b * h) / 2
    return area


def get_area_of_rectangle(b, h):
    area = b * h
    return area

'''
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
'''
