#!/usr/bin/env python2

def RecursiveListWithinListPrinter(*args, **kwargs):
    for outerList in list(args)+list(kwargs.items()):
        if type(outerList) == list:
            for innerList in outerList:
                if type(innerList) == list:
                    RecursiveListWithinListPrinter(innerList)
                else:
                    print(innerList)


l = [1,2,3,4,5]
RecursiveListWithinListPrinter(l)
