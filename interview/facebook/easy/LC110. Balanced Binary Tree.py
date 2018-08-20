class Solution(object):
	def isBalanced(self, root):
		if not root:
			return True
		return self.maxDepth(root)!= -1
		
	def maxDepth(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if not root:
			return 0
		left = self.maxDepth(root.left)
		right = self.maxDepth(root.right)
		if left == -1 or right == -1 or abs(left - right) > 1:
			return -1
		return max(left,right)+1