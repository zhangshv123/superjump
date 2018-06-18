# find the cycle given a directed graph and the node (find the path without storing the paths on the fly)
from collections import defaultdict
class Node:
    def __init__(self):
        self.children = defaultdict(Node)
def findCycle(root):
    stk, array = [(root, 0)], []
    while len(stk) > 0:
        cur, height = stk.pop()
        if height >= len(array):
            array.append(cur)
        else:
            array[height] = cur
        for c in cur.children.values():
            if c in array:
                return array[array.index(c):]
            stk.append((c, height + 1))
a = Node()
b = Node()
c = Node()
a.children['b'] = b
b.children['c'] = c
c.children['b'] = b
print(a, b, c)
print(findCycle(a))