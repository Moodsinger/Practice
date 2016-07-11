#!/usr/bin/env python

from ABC import ABCMeta, abstractmethod
from singelton import Singelton

class Node(object, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        self.value = None

@Singelton
class Root(Node):
    def __init__(self):
        Node.__init__()

class SubNode(Node):
    def __init__(self):
        Node.__init__()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Functions

def GenTree(depth, base):
    if depth == 0:
        y = Root()
        return y
    else:
        nodes = (depth)*base
        for i in xrange(nodes):
            nodes_at_depth = {}
            nodes_at_depth[str(depth)+'_instance_'+str(i)] = SubNode()
        return GenTree(depth-1, base)
