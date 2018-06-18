 #!/usr/bin/python
"""
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

         1
        / \
      /   \
     0 --- 2
            / \
            \_/
"""
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

"""
method 1, combine create node and add relation together
"""
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneNode(self, node, node_map):
        if node is None:
            return None
        if node in node_map:
            return node_map[node]
        newNode = UndirectedGraphNode(node.label)
        node_map[node] = newNode
        for neighbor in node.neighbors:
            newNode.neighbors.append(self.cloneNode(neighbor, node_map))
        return newNode
    
    def cloneGraph(self, node):
        node_map = {}
        return self.cloneNode(node, node_map)

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def dfs_createNode(self, node, clone_map):
        if node not in clone_map:
            clone_map[node] = UndirectedGraphNode(node.label)
            for neighbor in node.neighbors:
                self.dfs_createNode(neighbor, clone_map)
    def cloneGraph(self, node):
        if node is None:
            return None
        clone_map = dict()
        self.dfs_createNode(node, clone_map)
        # clone neighbors
        for n in clone_map:
            new_node = clone_map[n]
            for neighbor in n.neighbors:
                new_node.neighbors.append(clone_map[neighbor])
        return clone_map[node]