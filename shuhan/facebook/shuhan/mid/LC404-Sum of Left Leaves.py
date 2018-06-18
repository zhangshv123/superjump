#!/usr/bin/python
class Solution(object):
	def sumOfLeftLeaves(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		ans = 0
		if root: 
			l, r = root.left, root.right
			if l and (l.left or l.right) is None:
				ans += l.val
			ans += self.sumOfLeftLeaves(l) + self.sumOfLeftLeaves(r)
		return ans
