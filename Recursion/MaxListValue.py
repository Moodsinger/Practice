#!/usr/bin/env python2
# def MaxValueOf(l):
#     if (l) and len(l) == 1:
#         return l[0]
#     else:
#         B = l[1:len(l)]
#         return MaxValueOf(B)
#
# l = [0,1,3,2]
# print(MaxValueOf(l))
#
# def MVO(l):
#     for i in range(0, len(l)):
#         try:
#             if l[i] > l[i+1]:
#                 maxVal = l[i]
#         except:
#             pass
#     print(maxVal)
#
# MVO([1,3,2])

def Max(list):
    if len(list) == 1:
        return list[0]
    else:
        m = Max(list[1:])
        return m if m > list[0] else list[0]

def main():
    list = eval(raw_input(" please enter a list of numbers: "))
    print("the largest number is: ", Max(list))

main()
