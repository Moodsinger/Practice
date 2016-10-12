#!/usr/bin/env python

from math import sqrt

'''
    GOAL: Just checking for triangle numbers that are also perfect squares
'''


def sqtri():
    y = 10000000
    lst_numbers = []
    for i in range(int(y)):
        x = (i*(i+1))//2    # This is a method to check for triangle numbers
        if type(sqrt(x)) == int:        # This line should be if int(sqrt(x))**2 == x:
            print(str(x) + " is a triangle number and a square number")
            lst_numbers.append(x)
    if type(lst_numbers) == list:
        return lst_numbers
    else:
        return 1

def patternTesting(lst_num):
    x = []
    if type(lst_num) == list:
        for i in range(len(lst_num)):
            if type(i) == int:
                try:
                    chk = lst_num[i+1] - lst_num[i]
                    if int(chk**2) in lst_num:
                        print(str(chk) + " is in our list!")
                        x.insert(int(chk))              # This should be append
                except:
                    pass
                return x
            else:
                return 1
    else:
        print("How was that not a list?")
        print(type(lst_num))
    return x

# Write a method to see if this is a Geometric Series or not

def chkGeoSeries(listofnumbers):
    pass

a = sqtri()
b = patternTesting(a)
