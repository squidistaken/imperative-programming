x1 = float(input("Circle 1 x: "))
y1 = float(input("Circle 1 y: "))
r1 = float(input("Circle 1 radius: "))

x2 = float(input("Circle 2 x: "))
y2 = float(input("Circle 2 y: "))
r2 = float(input("Circle 2 radius: "))

dx = x1 - x2
dy = y1 - y2
r = r1 + r2

if dx*dx + dy*dy <= r*r:
    print("Overlap!")
else:
    print("No overlap!")
