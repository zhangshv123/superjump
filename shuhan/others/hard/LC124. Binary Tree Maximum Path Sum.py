#!/usr/bin/python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def maxPathSum(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		
		return self.helper(root)[1]
	
	def helper(self,root):
		if not root:
			return (0,-sys.maxint)
#		local代表以我为结尾最大的，或者可以不包含我
#		global代表题目所求的，必须包含我的最大的
		localLeftMax,globalLeftMax = self.helper(root.left)
		localRightMax,globalRightMax = self.helper(root.right)
		localMax = max(max(localLeftMax,localRightMax)+root.val,0)
		globalMax = max(globalLeftMax,globalRightMax,localLeftMax+localRightMax+root.val)
		return (localMax,globalMax)
		
		
	
	
		
