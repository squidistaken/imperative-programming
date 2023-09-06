'''
File: moneyformatter.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    This program formats float numbers in terms of euros and cents.
'''

print("Please enter a number. Preferably a float!")
money_value = float(input("Your number: "))
euro = int(money_value)
# For the cent, I subtracted money_value with the new int euro, leaving only the decimal.
# This is then multiplied by 100 to create a whole number (assuming we aren't dealing with thousandths and beyond).
# It is then rounded and converted to an integer. I had to round first due to the behaviour the int function does.
cent = int(round((money_value - euro) * 100))

print(euro, "euro", cent)
