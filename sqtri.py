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
'''
    NEW GOAL: Find the pattern in the result... FIND IT!
'''


def patternTesting(lst_num):
    '''
        Test one, get the list of consecutive sqtri numbers whose, get ready for this,
        absolute difference squared is a sqtri number
    '''
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
                print("How was that not a list?")
                return 1
    else:
        print(type(lst_num))
    return x

# Write a method to see if this is a Geometric Series or not

def chkGeoSeries(listofnumbers):
    lst_bool = []
    indicies_out_of_range = []
    for number in len(listofnumbers):
        ind = number -1
        try:
            if (listofnumbers[ind+1]/listofnumbers[ind]) == (listofnumbers[ind+2]/listofnumbers[ind+1])
                list_bool.append(True)
            else:
                list_bool.append[False]
        except KeyError:
            indicies_out_of_range.append(ind)
    if False in lst_bool:
        return 0
    else:
        return 1


a = sqtri()
b = patternTesting(a)
