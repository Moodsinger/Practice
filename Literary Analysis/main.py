#!/usr/bin/env python2

# Initialize all the variables
path = raw_input("Please write the location of the file from the root directory: ")
f = open(str(path), 'r')
l = f.read()
i = l.split('\n')
ID = 0              # ID of each item
count = 0           # Number of times it came
done = []
# Now the method
j = i.sort()
for a in j:
    print str(ID) + " " + i[a]
    ID += 1
    done.append(str(ID))
