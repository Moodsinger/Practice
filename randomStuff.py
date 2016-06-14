#!/usr/bin/env python

class Transition(object):                                       # A transition class. Just in case we have to do
    def __init__(self, toState, *args, **kwargs):               # Something when we are changing states. Like say
        self.toState = toState                                  # from the Mapping state to the Finding state.

    def Execute(self, *args, **kwargs):
        print("Transitioning to %d", %(self.toState))

class BaseState(object):                                        # This will be a Base state class from which all
    def __init__(self, *args, **kwargs):                        # states will inherit.
        pass                                                    # It's empty because in the end, when I'm cleaning it up,
                                                                # I'll look at what's common and put it here
class Mapping(object):
    def __init__(self, blockedCells, gridX, gridY, *args, **kwargs):
        self.wholeMap = []                                      # A list to store every (X,Y) coordinate in a tuple
                                                                # So it'll be tuples inside of lists
    def MapWholeMap(self, *args, **kwargs):                     # This will just go through the two coordinates and map them
        for i in xrange(gridX):
            for j in xrange(gridY):
                self.wholeMap.append((gridX, gridY))

    def RemoveBlockedCells(self):                               # This will remove any cells that are blocked, i.e, you cannot
        if type(blockedCells) == list:                          # Go on them
            for blockedCell in blockedCells:
                if type(blockedCell) == tuple:
                    self.wholeMap.pop(wholeMap.index[blockedCell])


class Finding(object):
    def __init__(self, currentCell, *args, **kwargs):
        self.currentCell = currentCell
        if type(currentCell) != tuple:                          # This is pretty simple, just make sure that it's a tuple
            self.currentCellList = tuple(currentCell) # The list will store [x,y]

    def CheckingNeighbouringCells(self, *args, **kwargs):
        testingCell = [currentCell]                             # Here, change X, Y coordinates and see which neighbouring cell is the
        try:                                                    # closest
            pass
        except:
            pass
