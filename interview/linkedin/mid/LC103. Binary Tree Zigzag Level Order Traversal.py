# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
	def zigzagLevelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		if not root:
			return []
		q = deque()
		q.append(root)
		res = []
		level = 0
		while len(q) > 0:
			size = len(q)
			level += 1
			path = []
			for i in range(size):
				cur = q.popleft()
				path.append(cur.val)
				if cur.left:
					q.append(cur.left)
				if cur.right:
					q.append(cur.right)
			if level%2 == 0:
				path = list(reversed(path))
			res.append(path)
		return res
					
			
