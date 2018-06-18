#!/usr/bin/python
"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of 
nodes), write a function to check whether these edges make up a valid tree.

For example:

Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.
"""
"""
判断输入的边是否能构成一个树，我们需要确定两件事：

1.这些边是否构成环路，如果有环则不能构成树
2.这些边是否能将所有节点连通，如果有不能连通的节点则不能构成树
因为不需要知道具体的树长什么样子，只要知道连通的关系，所以并查集相比深度优先搜索是更好的方法

我们再来看Union Find的方法，这种方法对于解决连通图的问题很有效，思想是我们遍历节点，如果两个节点相连，
我们将其roots值连上，这样可以帮助我们找到环，我们初始化roots数组为-1，然后对于一个pair的两个节点分别调用find函数，
得到的值如果相同的话，则说明环存在，返回false，不同的话，我们将其roots值union上
"""
from collections import defaultdict
class Solution:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        parent = defaultdict(lambda: -1)
        def findRoot(n):
            while parent[n] != -1:
                n = parent[n]
            return n
        for a, b in edges:
            x, y = findRoot(a), findRoot(b)
            if x == y:
                return False
            parent[x] = y
        return n - 1 == len(edges)

#变形： 找树中多余的一条edge.  