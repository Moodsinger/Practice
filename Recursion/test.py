#!/usr/bin/env python2

def Func(l, *args, **kwargs):
    for i in l:
        if type(i) != list:
            print i
        else:
            for j in i:
                print j

def FuncDispather(l, *args, **kwargs):
    a = 0
    size = len(l)
    while(a<size-1):
        Func(l)
    print()




Func([1,[2,3], [4,5]])
