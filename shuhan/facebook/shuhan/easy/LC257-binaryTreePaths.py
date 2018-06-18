#!/usr/bin/python
class Solution(object):
	def binaryTreePaths(self, root):
		res = []
		if root:
			self.helper(root,res,[])
		return res
	
	def helper(self,root,res,path):
		path.append(str(root.val))
		
		if not root.left and not root.right:
			res.append("->".join(path))
			path.pop()
			return
		
		if root.left:
			self.helper(root.left, res, path)
		if root.right:
			self.helper(root.right, res, path)
		path.pop()
		
