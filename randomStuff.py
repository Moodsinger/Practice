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
    def __init__(self, blockedCells, gridX, gridY, *args, **kwargs):
        self.wholeMap = []

    def MapWholeMap(self):
        for i in xrange(gridX):
            for j in xrange(gridY):
                self.wholeMap.append((gridX, gridY))

    def RemoveBlockedCells(self):
        if type(blockedCells) == list:
            for blockedCell in blockedCells:
                if type(blockedCell) == tuple:
                    self.wholeMap.pop(wholeMap.index[blockedCell])


class Finding(object):
    def __init__(self, currentCell):
        self.currentCell = currentCell
        if type(currentCell) != list:
            self.currentCellList = list(currentCell) # The list will store [x,y]

    def CheckingNeighbouringCells(self):
        testingCell = [currentCell]
        try:
            pass
        except:
            pass
