#!/usr/bin/env python

def ForbidNodes(dictionary, path):
    forbidden_nodes = []
    if type(dictionary) == dict:
        for key, value in dictionary.items():
            for i in path:
                if value = path[-1]:
                    forbidden_nodes.append(value)
    if type(forbidden_nodes) == list:
        return forbidden_nodes
    else:
        return 1;
