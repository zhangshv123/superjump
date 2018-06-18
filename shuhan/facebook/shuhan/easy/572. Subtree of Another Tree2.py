#!/usr/bin/python
class Solution(object):
	def isSubtree(self, s, t):
		prePathS = self.generatePre(s)
		prePathT = self.generatePre(t)
		return prePathT in prePathS
	
	def generatePre(self,m):
		res = ""
		stack = []
		stack.append(m)
		while stack :
			cur = stack.pop()
			if not cur:
				res += ",#" #一定要加逗号，不然[12]和[2]这样的不行！
			else:
				res += ","+str(cur.val)
				stack.append(cur.left)
				stack.append(cur.right)
		return res			