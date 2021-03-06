#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod
from singleton import Singleton
from dis import dis
from ListWithinListPrinter import *
'''
    This section just has the required classes I want for this file
    It contains an abstract class called Node which should never be
    instantiated (I dunno if that's the correct spelling) because it
    won't tell if any given node is a Root Node or a Sub-Node.
'''


class Node(object):
    '''
        The is an abstract class (i.e, can't be instanciated) because
        this would be the base class of any node. this should only serve
        as a base class.
    '''
    __metaclass__ = ABCMeta
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
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Functions

def GenTree(depth , base):
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
        nodes = (depth)*base
        for i in range(nodes):
            nodes_at_depth[int(100*depth+(i))] = SubNode()
        return [GenTree(depth-1, base), nodes_at_depth]

def map_values(di_nodes, lst_values):
    '''
        This code feels like it's really bad...
        especially the else statement...
    '''
    if type(di_nodes) == dict:
        if len(lst_values) == len(di_nodes):
            if type(di_nodes) == dict:
                print(type(di_nodes))
                new_lst_values = lst_values[:int(len(di_nodes))-1]
                for key, value in di_nodes:
                    value.Value = lst_values[int(str(key)[-1]-1)]
                    di_nodes[key] = value.Value
    return di_nodes

# I should really get to debugging this..
def Nav(di_nodes):
    '''
        I'm just going to do it for a binary tree, and then make a general method
        Okay. Pick off from here next time:
        Apparently, each set of subnodes have their own dictionary..
        how the fuck did I manage that?
    '''
    path = []
    if type(di_nodes) == dict:
        for key, value in di_nodes.items():
            if int(key) % 2 == 0:
                try:
                    if(di_nodes[key+100]) > (di_nodes[key+101]):
                        path.append(di_nodes[key+100])
                    else:
                        path.append(di_nodes[key+101])
                except KeyError:
                    print(key)
            else:
                int(key)+1
        return path
    else:
        print("Dude, that wasn't a dictionary")
        return 1

def summation(lst):
    total = 0
    for i in lst:
        total += i
    return total

if __name__ == "__main__":
    depth = 5
    base = 2
    tree = GenTree(depth, base)
    print(tree)
    lst_values = [1,2,3,4,5,6,7,6,5,4,3,2,1]
    map_values_instance = map_values(tree[1], lst_values)
    final_path = Nav(tree[1])
    print(final_path)
    print(summation(final_path))
    #dis(GenTree)
    RecursiveListWithinListPrinter(tree)
    input("Press enter")
