#!/usr/bin/env python

from math import sqrt

def sqtri():
    y = 1000
    lst_numbers = []
    for i in range(int(y)):
        x = (i*(i+1))//2
        if int(sqrt(x))**2 == x:
            print(str(x) + " is a triangle number and a square number")
            lst_numbers.append(x)

def patternTesting(lst_num):
    x = []
    if type(lst_num) == list:
        for i in range(len(lst_num)):
            if type(i) == int:
                try:
                    chk = lst_num[i] - lst_num[i+1]
                    if int(chk**2) in lst_num:
                        print(str(chk) + " is in our list!")
                        x.append(int(chk))
                except:
                    print("something went wrong")
    return x

a = sqtri()
b = patternTesting(a)
input("press enter")
