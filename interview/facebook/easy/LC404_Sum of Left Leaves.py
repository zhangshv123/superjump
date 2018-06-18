"""
Find the sum of all left leaves in a given binary tree.

Example:

	3
   / \
  9  20
	/  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def isLeave(self, root):
		if root is not None and root.left is None and root.right is None:
			return True
		return False
	def sumOfLeftLeaves(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if root is None:
			return 0
		sum_leftLeaves = 0
		if self.isLeave(root.left):
			sum_leftLeaves += root.left.val
		else:
			sum_leftLeaves += self.sumOfLeftLeaves(root.left)
		sum_leftLeaves += self.sumOfLeftLeaves(root.right)
		return sum_leftLeaves