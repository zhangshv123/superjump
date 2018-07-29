#!/usr/bin/python
class Solution(object):
	counter = 0
	def pathSum(self, root, sum):
		if not root:
			return self.counter
		if root:
			self.helper(root, sum)
		return self.counter
		
	
	def helper(self, node, target):
		if not node.left and not node.right:
			if node.val == target:
				self.counter += 1
			return [node.val]
		left,right = [], []
		if node.left:
			left = self.helper(node.left,target)
		if node.right:
			right = self.helper(node.right,target)
		pathSum = []
		pathSum.append(node.val)
		if left:
			for v in left:
				pathSum.append(v+node.val)
		if right:
			for v in right:
				pathSum.append(v+node.val)
		for v in pathSum:
			if v == target:
				self.counter += 1
		return pathSum
