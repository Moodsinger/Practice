#!/usr/bin/env python2

from random import randint

print("\t\tThe guessing game")

num = raw_input("Enter an integer between 1 and 10: ")
ans = randint(0, 10)
c   = 0

while(int(num) != int(ans)):
    if int(num) > int(ans):
        print("too High")
    elif int(num) < int(ans):
        print("Too low ")

    num = raw_input("Enter an integer between 1 and 10: ")
    c += 1

print("Congratulations, you got it in " + str(c) + " guesses")
