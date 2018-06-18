"""
经典面经题，一个doubly linked list, 可能无限长，input是an array of reference to the list nodes. 排出一个cluster。楼主用的BFS做的，于是时间复杂度还被面试官误导了一下没有坚持自己的看法。。
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
def getCluster(nodes):
    res = []
    visited = set()
    while len(nodes) > 0:
        cur = nodes.pop()
        if cur in visited:
            continue
        cluster = [cur]
        visited.add(cur)
        left, right = cur.prev, cur.next
        while left in nodes:
            cluster.append(left)
            visited.add(left)
            left = left.prev
        while right in nodes:
            cluster.append(right)
            visited.add(right)
            right = right.next
        res.append(cluster)
    return res
a, b, c, d, e = Node("a"), Node("b"), Node("c"), Node("d"), Node("e")
a.next, b.next, c.next, d.next = b, c, d, e
b.prev, c.prev, d.prev, e.prev = a, b, c, d
print(len(getCluster([b, d, e])))