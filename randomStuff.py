    #!/usr/bin/env python

# class Transition(object):                                       # A transition class. Just in case we have to do
#     def __init__(self, toState, *args, **kwargs):               # Something when we are changing states. Like say
#         self.toState = toState                                  # from the Mapping state to the Finding state.
#
#     def Execute(self, *args, **kwargs):
#         print("Transitioning to %d", %(self.toState))
#
# class BaseState(object):                                        # This will be a Base state class from which all
#     def __init__(self, *args, **kwargs):                        # states will inherit.
#         pass                                                    # It's empty because in the end, when I'm cleaning it up,
#                                                                 # I'll look at what's common and put it here

# DATE:
class Map(object):
    '''
        A list to store every (X,Y) coordinate in a tuple
        So it'll be tuples inside of lists
        This will just go through the two coordinates and map them
    '''
    def __init__(self, blockedCells, gridX, gridY, *args, **kwargs):
        self.wholeMap = []
        MapWholeMap()
        RemoveBlockedCells()

    def MapWholeMap(self, *args, **kwargs):
        for i in xrange(gridX):
            for j in xrange(gridY):
                self.wholeMap.append((gridX, gridY))
        return self.wholeMap

    def RemoveBlockedCells(self):
        '''
        This will remove any cells that are blocked, i.e, you cannot
        Go on them
        '''
        if type(blockedCells) == list:
            for blockedCell in blockedCells:
                if type(blockedCell) == tuple:
                    self.wholeMap.pop(wholeMap.index[blockedCell])


class Find(object):
    '''
    This is pretty simple, just make sure that it's a tuple
    The list will store [x,y]
    '''
    def __init__(self, currentCell, goal, *args, **kwargs):
        self.currentCell = tuple(currentCell)
        self.goal = tuple(goal)



    def GenChildren(self, *args, **kwargs):
        '''
            Here, change X, Y coordinates and see which neighbouring cell is the
            Okay, firstly, a simple method to get children

        '''
        pass

    def getHeursitic(self, tempCurCell=0):
        '''
            Get heuristics for X, Y and then store them in a tuple
        '''
        try:
            self.heuristicX = abs(self.goal[0] - self.tempCurCell[0])
            self.heuristicY = abs(self.goal[1] - self.tempCurCell[1])
            self.heuristic = (self.heuristicX, self.heuristicY)
            return self.heuristic

        except:
            self.heuristicX = abs(self.goal[0] - self.currentCell[0])
            self.heuristicY = abs(self.goal[1] - self.currentCell[1])
            self.heuristic = (self.heuristicX, self.heuristicY)
            return self.heuristic


    def FindPath(self):
        self.priorityDict = {int(priority):self.currentCell}

if __name__ == '__main__':
    # what the hell did I do here?
    # Was I high?
    x = 5
    y = 5
    blockedcells =  [(1,1)]
    mapIt = Map(blockedcells, x, y)


x = Find((1,1), (5,5))
print(x.getHeursitic())
