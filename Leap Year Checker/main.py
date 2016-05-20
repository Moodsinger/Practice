#!/usr/bin/env python2
year = raw_input("Enter a year: ")
# 1) divisible by 4
# 2) not divisible by 100
# 3) but if it is divisible by 400

if(int(year) % 4 == 0):
    if(int(year) % 100 == 0):
        if(int(year) % 400 == 0):
            print('It\'s a leap year!')
    print("It's a leap year!")
else:
    print('Nope, not a leap year')
