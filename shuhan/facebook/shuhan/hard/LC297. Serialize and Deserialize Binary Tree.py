# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:
	def serialize(self, root):
		"""Encodes a tree to a single string.
		
		:type root: TreeNode
		:rtype: str
		"""
		res = []
		q = deque()
		q.append(root)
		while len(q)>0:
			cur = q.popleft()
			if cur:
				res.append(str(cur.val))
				q.append(cur.left)
				q.append(cur.right)
			else:
				res.append("null")
		return "["+",".join(res)+"]"
		
	def deserialize(self, data):
		"""Decodes your encoded data to tree.
		
		:type data: str
		:rtype: TreeNode
		"""
		nodes = []
		for node in data[1:-1].split(","): #去掉"["和“]”只保留中间的所有
			if node != "null":
				nodes.append(TreeNode(int(node)))
			else:
				nodes.append(None)
		q = deque()
		q.append(nodes[0])
		index = 0
		while len(q)>0:
			size = len(q)
			for i in range(size):
				cur = q.popleft()
				if cur :
					cur.left = nodes[index+1]
					cur.right = nodes[index+2]
					q.append(cur.left)
					q.append(cur.right)
					index +=2
		return nodes[0]
					
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))