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
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Functions
global nodes_at_depth;
def GenTree(depth, base):
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
        nodes = (depth+1)*base
        for i in range(depth):
            nodes_lst.append(i)
        for i in range(nodes):
            nodes_at_depth[str(depth)+'_instance_'+str(i)] = SubNode()
        return [GenTree(depth-1, base), nodes_at_depth]

f = GenTree(2,2)
'''
    From the following statement I do get a bunch of Instances of
    SubNode() but not the way I want them to generate
'''
print(f)
'''
    The following line should print out the second instance of
    the second, layer maybe? But it just says key error
'''
print(f[1]['1_instance_'])

def Nav(di_nodes):
    pass
