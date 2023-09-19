'''
File: rps.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    This program emulates rock, paper, scissors.
'''

option_1 = str(input())
option_2 = str(input())

match option_1, option_2:
    case "rock", "scissors":
        print("Player one wins.")
    case "rock", "paper":
        print("Player two wins.")
    case "paper", "scissors":
        print("Player two wins.")
    case "paper", "rock":
        print("Player one wins.")
    case "scissors", "rock":
        print("Player two wins.")
    case "scissors", "paper":
        print("Player one wins.")
    case default:
        print("It is a draw.")
