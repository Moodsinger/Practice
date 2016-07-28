#!/usr/bin/env python

from abc import ABCMeta, abstractmethod
from singleton import Singleton
'''
    This section just has the required classes I want for this file
    It contains an abstract class called Node which should never be
    instantiated (I dunno if that's the correct spelling) because it
    won't tell if any given node is a Root Node or a Sub-Node.
'''


class Node(object, metaclass=ABCMeta):
    '''
        The is an abstract class (i.e, can't be instanciated) because
        this would be the base class of any node. this should only serve
        as a base class.
    '''
    @abstractmethod
    def __init__(self):
        self.value = None

@Singleton # The root node is a Singelton for obvious reasons
class Root(Node):
    def __init__(self):
        Node.__init__(self)
#And now just a simple node class
class SubNode(Node):
    def __init__(self):
        Node.__init__(self)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Functions

def GenTree(depth = 0, base = 0):
    '''
        Function to generate a tree structure with any give base
        It will create the required number of nodes at any depth,
        and then return those nodes (which are just instances of the class
        SubNode() defined up above) and also it will return an instance of
        this function with the depth subtracted. So we should have stop
        once we reach the root node
    '''
    nodes_at_depth = {}
    if depth == 0:
        y = Root()
        return y
    else:
        nodes_lst = []
        nodes = (depth)*base
        for i in range(depth):
            nodes_lst.append(i)
        for i in range(nodes):
            nodes_at_depth[int(100*depth+(i+1))] = SubNode()
        return [GenTree(depth-1, base), nodes_at_depth]

def Nav(di_nodes, depth = 0, base = 0):
    '''
        I'm just going to do it for a binary tree, and then move it to a general sense
    '''
    path = []
    if type(di_nodes) == dict:
        for key, value in di_nodes.items():
            if(di_nodes[key+100]) > (di_nodes[key+101]):
                path.append(di_nodes[key+100])
            else:
                path.append(di_nodes[key+101])
        return path
    else:
        print("Dude, that wasn't a dictionary")
        return 1

def summation(lst):
    total = 0
    for i in lst:
        total += i

if __name__ == "__main__":
    depth = 3
    base = 2
    tree = GenTree(depth, base)
    final_path = Nav(tree[1], depth, base)
    summation(final_path)
