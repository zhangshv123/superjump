"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure 
and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all 
of this node's descendants. The tree s could also be considered as a subtree of itself.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def isSubtree(self, s, t):
		"""
		:type s: TreeNode
		:type t: TreeNode
		:rtype: bool
		"""
		if not s:
			return False
		if self.isSame(s,t):
			return True
		return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
		
	
	def isSame(self,s,t):
		if not s and not t:
			return True
		if not s or not t:
			return False
		if s.val == t.val:
			return self.isSame(s.left,t.left) and self.isSame(s.right,t.right)
		return False
"""
 follow up是如何分别check一堆树是不是一个树的subtree。 时间要求O(m + n)
N是被CHECK的母树的节点数，M是有M个输入的树（as a list）
加size是可以减少复杂度的但是这里还不够
我的做法是encode母树，hash成一个字符串，子树也encode然后比较。面试官很同意。
面试官的想法是一个叫Bloom filter的东西你可以看看
"""
		