#!/usr/bin/python
class Solution:
	"""
	@param root: the root of the binary tree
	@return: all root-to-leaf paths
	"""
	def binaryTreePaths(self, root):
		# write your code here
		res = []
		
		if not root:
			return res
		
		if not root.left and not root.right:
			res.append(str(root.val)) #易错点：这里是返回void
			return res
		
		left_paths = self.binaryTreePaths(root.left)
		right_paths = self.binaryTreePaths(root.right)
		
		for path in left_paths:
			path = str(root.val) + "->"+path
			res.append(path)
			
		for path in right_paths:
			path = str(root.val) + "->"+ path
			res.append(path)
			
		return res
