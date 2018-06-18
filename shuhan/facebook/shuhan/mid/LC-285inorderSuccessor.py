#!/usr/bin/python
class Solution(object):
	def inorderSuccessor(self, root, p):
		"""
		:type root: TreeNode
		:type p: TreeNode
		:rtype: TreeNode
		"""
		if root == None:
			return None
		if root.val <= p.val:
			return self.inorderSuccessor(root.right,p)
		else:
			left = self.inorderSuccessor(root.left,p)
			return left if left != None else root