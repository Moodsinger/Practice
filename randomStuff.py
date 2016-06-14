#!/usr/bin/env python

class Transition(object):
    def __init__(self, toState):
        self.toState = toState

    def Execute(self):
        print("Transitioning to %d", %(self.toState))

class BaseState(object):
    def __init__(self):
        pass

class Mapping(object):
    def __init__(self, blockedCells, *args, **kwargs):
        wholeMap = []
        if type(blockedCells) == list:
            for blockedCell in blockedCells:
                if type(blockedCell) == tuple:
                    wholeMap.pop(wholeMap.index[blockedCell])


class Finding(object):
    def __init__(self, currentCell):
        self.currentCell = currentCell
        if type(currentCell) != list:
            self.currentCellList = list(currentCell) # The list will store [x,y]

    def CheckingNeighbouringCells(self):
        testingCell = [currentCell]
        try:
            while
