
"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.

Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given undirected graph will be like this:
  1
 / \
2 - 3
Example 2:
Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
Output: [1,4]
Explanation: The given undirected graph will be like this:
5 - 1 - 2
    |   |
"""
from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        union_map = defaultdict(lambda : -1)
        def findRoot(i):
            root = i
            while union_map[root] != -1:
                root = union_map[root]
            return root
        for edge in edges:
            r1, r2 = findRoot(edge[0]), findRoot(edge[1])
            if r1 == r2:
                return edge
            union_map[r1] = r2

"""
directed graph
II
"""
"""
1) Check whether there is a node having two parents. 
    If so, store them as candidates A and B, and set the second edge invalid. 
2) Perform normal union find. 
    If the tree is now valid 
           simply return candidate B
    else if candidates not existing 
           we find a circle, return current edge; 
    else 
           remove candidate A instead of B.
"""

class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        can1 = [-1, -1]
        can2 = [-1, -1]
        parent = [0 for _ in range(len(edges) + 1)]
        # step 1, check whether there is a node with two parents
        for i in range(len(edges)):
            if parent[edges[i][1]] == 0:
                parent[edges[i][1]] = edges[i][0]
            else:
                can2 = (edges[i][0], edges[i][1])
                can1 = (parent[edges[i][1]], edges[i][1])
                edges[i][1] = 0
        # step 2, union find                
        for i in range(len(edges)):
            parent[i] = i
        for i in range(len(edges)):
            if edges[i][1] == 0:
                continue
            child = edges[i][1]
            father = edges[i][0]
            # Now every node only has 1 parent, so root of v is implicitly v
            # if candidate exit, it implies it shows up in the loop(can1)
            if self.root(parent, father) == child:
                if can1[0] == -1:
                    return edges[i]
                return can1
            parent[child] = father
        return can2
    def root(self, parent, i):
        while i != parent[i]:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
