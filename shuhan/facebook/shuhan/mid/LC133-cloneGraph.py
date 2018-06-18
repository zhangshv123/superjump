#!/usr/bin/python
class Solution:
#	注意，这道题和Copy List with Random Pointer  那题很像
	def cloneGraph(self, node):
		d = dict()
		return self.clone(node,d)
			
	def clone(self, node,d):
		if node == None :
			return node
				
		if node in d:
			return d[node]
				
		newNode = UndirectedGraphNode(node.label)
		d[node] = newNode
		for neighbor in node.neighbors:
			newNode.neighbors.append(self.clone(neighbor,d))
		return newNode