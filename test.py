#!/usr/bin/env python

class baseClass1(object):
    """docstring for baseClass1"""
    def __init__(self):
        self.x = 12

class BaseClass2(object):
    def __init__(self):
        self.x = 14

class InClass1(baseClass1, BaseClass2):
    def __init__(self):
        super(InClass1, self).__init__()
        print(self.x)

class InClass2(baseClass1, BaseClass2):
    def __init__(self):
        baseClass1.__init__(self)
        print("From base class 1 of InClass2: " + str(self.x))
        BaseClass2.__init__(self)
        print("From base class 2 of InClass2: " + str(self.x))

g = InClass1()
gg = InClass2()
