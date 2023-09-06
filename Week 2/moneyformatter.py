'''
File: moneyformatter.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    This program formats float numbers in terms of euros and cents.
'''

print("Please enter a number. Preferably a float!")
money_value = float(input("Your number: "))
euro = int(money_value)
cent = int(round((money_value - euro) * 100))

print(euro, "euro", cent)
