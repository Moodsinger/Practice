#!/usr/bin/env python

import re

f = open("/home/jatinubuntu/Documents/file.html")
text = f.read()
x = re.split(r'[0-9<>\\/;: ]', text)
print(type(x))
try:
    for i in len(x):
        if x[i] == '' or x[i] == ' ':
            x.pop(i)
except:
    print("It didn't work :(")

print(x)
