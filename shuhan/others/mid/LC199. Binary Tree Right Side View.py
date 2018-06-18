#!/usr/bin/python
#DFS做法：
class Solution(object):
	def rightSideView(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		res = []
		if root !=None:
			right = self.rightSideView(root.right)
			left = self.rightSideView(root.left)#只把左边比右边长的放进去
			res =  [root.val]+right+left[len(right):]
		return res
#TOPDOWN做法
class Solution(object):
	def rightSideView(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		res,stk = [],[]
#		这里global array就是res自己，从右往左扫，全部答案放在global array里面，最后输出就好
		if root:
			stk.append((root,0))
			while len(stk) > 0:
				node,height = stk.pop()
				if len(res) <= height:
					res.append(node.val)
				else:
					res[height] = node.val
				if node.right:
					stk.append((node.right,height+1))
				if node.left:
					stk.append((node.left,height+1))
		return res
#BFS做法
from collections import deque
class Solution(object):
	def rightSideView(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		res,q = [],deque()
		if root:
			q.append(root)
		while len(q) > 0:
			size = len(q)
			res.append(q[-1].val)
			for i in range(size):
				node = q.popleft()
				if node.left:
					q.append(node.left)
				if node.right:
					q.append(node.right)
		return res