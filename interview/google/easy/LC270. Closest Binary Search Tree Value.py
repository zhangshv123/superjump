#!/usr/bin/python
class Solution(object):
	def closestValue(self, root, target):
		"""
		:type root: TreeNode
		:type target: float
		:rtype: int
		"""
		res = root.val
		
		while root:
			if abs(root.val - target) < abs(res - target):
				res = root.val
			
			root = root.left if root.val > target else root.right
			
		return res