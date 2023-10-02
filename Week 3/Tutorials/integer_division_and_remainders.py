def is_odd():
    num = int(input("Int: "))

    if num % 2 != 0:
        print(num, "is odd")
    else:
        print(num, "is even")


def is_divisor():
    x = int(input("x: "))
    y = int(input("y: "))

    if y % x == 0:
        print("x is a divisor of y.")
    else:
        print("x is not a divisor of y.")


def is_divisor_v2():
    x = int(input("x: "))
    y = int(input("y: "))
    z = int(input("z: "))

    if x * y * z == 0:
        print("Invalid")
    else:
        if y % x == 0 and z % y == 0:
            print("x is a divisor of y and y is a divisor of z.")
        elif (y % x) != (z % y == 0):
            print("Either x is a divisor of y or y is a divisor of z, but not both.")
        else:
            print("Invalid")


def last_or_second_last_digit_7():
    x = int(input("x: "))

    if x % 10 == 7:
        print("The last digit of x is 7.")
    elif x % 100 // 10 == 7:
        print("The second to last digit of x is 7.")
    else:
        print("Invalid.")


print("Select a claim."
      "\n1. x is odd"
      "\n2. x is a divisor of y"
      "\n3. x is a divisor of y and y is a divisor of z."
      "\n4. Either x is a divisor of y or y is a divisor of z, but not both."
      "\n5. The last digit of x is 7."
      "\n6. The second to last digit of x is 7.")
prompt = int(input())

match prompt:
    case 1:
        is_odd()
    case 2:
        is_divisor()
    case 3:
        is_divisor_v2()
    case 4:
        is_divisor_v2()
    case 5:
        last_or_second_last_digit_7()
    case 6:
        last_or_second_last_digit_7()
    case default:
        print("invalid.")
