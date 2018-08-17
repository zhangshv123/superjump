class Solution(object):
	def lowestCommonAncestor(self, root, p, q):
		if not root:
			return None
		while true:
			while root.val < min(p.val, q.val):
				if root.left:
					root = root.left
				else:
					return None
			while root.val > max(p.val, q.val):
				if root.right:
					root = root.left
			if root.val < min(p.val, q.val) and root.val < max(p.val, q.val):
				return root
		return None  
		
#iterative的版本：
class Solution(object):
	def lowestCommonAncestor(self, root, p, q):
		if not root:
			return None
		while True:
			while root.val < min(p.val, q.val):
				if root.left:
					root = root.right
			while root.val > max(p.val, q.val):
				if root.right:
					root = root.left
			if root.val >= min(p.val, q.val) and root.val <= max(p.val, q.val):
				return root
		return None  