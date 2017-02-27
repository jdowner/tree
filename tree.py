#!/usr/bin/python
# -*- coding: utf-8 -*-

import networkx as nx


def tree(root, children_func, label_func=str):
    """Writes a tree to standard out

    @param root          - the root node of the tree
    @param children_func - a function that takes a node and returns a list of
                           the nodes children
    @param label_func    - converts a node into a string (default=str)

    """
    def recurse(node, padding, last=False):
        if last:
            print(u"{}└── {}".format(padding[:-4], label_func(node)))
        else:
            print(u"{}├── {}".format(padding[:-4], label_func(node)))

        children = children_func(node)
        if children:
            for child in children[:-1]:
                recurse(child, padding + u"│   ", last=False)

            recurse(children[-1], padding + u"    ", last=True)

    recurse(root, u"    ", last=True)


graph = nx.DiGraph(["ac", "cd", "ce", "ab", 'ef','dg', 'dh'])
tree('a', graph.successors)


class Node(object):
    def __init__(self, label, children=None):
        self.label = label
        self.children = children or list()

    def __repr__(self):
        return self.label


root = Node('a', [
        Node('c', [
            Node('e', [
                Node('f'),
                ]),
            Node('d', [
                Node('g'),
                Node('h'),
                ]),
            ]),
        Node('b'),
    ])

tree(root, lambda node: node.children)


import yaml

graph = yaml.load("""
a:
- c:
  - e:
    - f
  - d:
    - g
    - h
- b
""")

def yaml_children(node):
    assert(isinstance(node, dict))
    assert(len(node.keys()) <= 1)

    _, successors = node.items()[0]

    children = list()
    for s in successors:
        if isinstance(s, dict):
            children.append(s)
            continue

        children.append({s:{}})

    return children


def yaml_label(node):
    try:
        return node.keys()[0]
    except Exception:
        return node


tree(graph, yaml_children, yaml_label)
