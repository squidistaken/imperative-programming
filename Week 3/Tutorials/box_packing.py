import math

# Calculate cube dimensions
cube_length = int(input("Cube length: "))

cube_volume = cube_length ** 3

# Calculate box dimensions
box_length = float(input("Box length: "))
box_width = float(input("Box width: "))
box_height = float(input("Box height: "))

# TODO: REDO WITHOUT MATH IMPORTED

box_volume = box_length * box_width * box_height

max_cubes = math.floor(box_volume / cube_volume)
box_volume_remaining = box_volume - (max_cubes * cube_volume)

print(max_cubes)
print(box_volume_remaining)
