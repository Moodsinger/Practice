#!/usr/bin/env python2
'''
def fib(x):
    if x==0:
        return 0
    elif x == 1:
        return 1

    return fib(x-1)+fib(x-2)

print(fib(1))
'''

#---------------------------------------------------------------------------------------------

def DigitCounter(x):
    if x < 10: return 1
    else:
        return DigitCounter(x/10) + 1

print(DigitCounter(111111111111111111))
