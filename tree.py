#!/usr/bin/python
# -*- coding: utf-8 -*-

import networkx as nx

graph = nx.DiGraph(["ac", "cd", "ce", "ab", 'ef','dg', 'dh'])

def tree(graph):
    def recurse(node, padding, last=False):
        if last:
            print(u"{}└── {}".format(padding[:-4], node))
        else:
            print(u"{}├── {}".format(padding[:-4], node))

        children = graph.successors(node)
        if children:
            for child in children[:-1]:
                recurse(child, padding + u"│   ", last=False)

            recurse(children[-1], padding + u"    ", last=True)

    recurse(graph.nodes()[0], u"    ", last=True)


tree(graph)
