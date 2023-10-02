price = int(input("Price in cents: "))

remainder = price % 5
price -= remainder

if remainder >= 3:
    price += 5

print(int(price))
