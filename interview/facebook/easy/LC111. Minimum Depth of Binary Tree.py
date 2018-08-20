class Solution(object):
	def minDepth(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if not root:
			return 0
		if not root.left:
			return self.minDepth(root.right)
		if not root.right:
			return self.minDepth(root.left)
		return min(self.minDepth(root.left),self.minDepth(root.right))+1