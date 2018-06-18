#!/usr/bin/python
class Solution:
	# @param root, a tree link node
	# @return nothing
	def connect(self, root):
		if not root:
			return 
		if root and root.left:
			root.left.next = root.right
			if root.next:
				root.right.next = root.next.left
			
		self.connect(root.left)
		self.connect(root.right)