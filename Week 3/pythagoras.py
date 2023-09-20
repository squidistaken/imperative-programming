a = int(input("Length 1: "))
b = int(input("Length 2: "))
c = int(input("Length 3: "))

a *= a  # a ** 2
b *= b
c *= c

if (a + b == c) or (a + c == b) or (b + c == a):
    print("Right angled triangle")
else:
    print("Not right angled triangle")
