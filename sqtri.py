#!/usr/bin/env python

from math import sqrt

def sqtri():
    y = input("Please enter max range: ")
    for i in range(int(y)):
        x = (i*(i+1))//2
        if int(sqrt(x))**2 == x:
            print(str(x) + " is a triangle number and a square number")

a = sqtri()
