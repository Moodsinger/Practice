#!/usr/bin/env python

def FirstReverse(_str):
    return _str[::-1]
print(FirstReverse('word'))

def FirstFactorial(num):
    if num in (0,1):
        return 1
    return num * FirstFactorial(num-1)

# keep this function call here
print(FirstFactorial(8))

def LongestWord(sen):

    x = sen.split()
    longest = 'didn\'t work'
    if type(x) == list:
        try:
            for i in range(len(x)):
                if len(x[i]) >= len(x[i+1]):
                    longest = x[i]
                else:
                    longest = x[i+1]
        except:
            pass
    return longest

print(LongestWord("I love dogs"))

lst = [1, 2, 3, 4]
def join(lst):
    if type(lst) == list:
        return ''.join(str(x) for x in lst)

print(join(lst))
