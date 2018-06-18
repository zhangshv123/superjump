# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	total = 0
	def diameterOfBinaryTree(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if root == None:
			return 0
		self.helper(root)
		return self.total
	
	def helper(self, root):  # gives the depth of the root's subtree
		leftDepth = 0 if root.left == None else self.helper(root.left)
		rightDepth = 0 if root.right == None else self.helper(root.right)
		localMax = leftDepth + rightDepth
		if localMax > self.total:
			self.total = localMax
		return max(leftDepth, rightDepth) + 1 #返回左右2边里面最长的路径
		
		
			
		
			