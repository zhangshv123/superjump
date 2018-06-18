#!/usr/bin/python
class Solution(object):
	def isSubtree(self, s, t):
		if not s :
			return False
		if self.isSame(s,t):
			return True
		else:
			return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
	
	def isSame(self,m,n):
		if not m and not n:
			return True
		if not m or not n:
			return False
		if m.val != n.val:
			return False
		else:
			return self.isSame(m.left,n.left) and self.isSame(m.right,n.right)