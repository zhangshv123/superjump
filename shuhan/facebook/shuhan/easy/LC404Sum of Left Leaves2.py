#BFS
from collections import deque
class Solution(object):
	def sumOfLeftLeaves(self, root):
		if not root or not root.left and not root.right:
			return 0
		res = 0
		queue = deque()
		queue.append(root)
		while queue:
			cur = queue.popleft()
			if cur.left and not cur.left.left and not cur.left.right:
				res += cur.left.val
			if cur.left:
				queue.append(cur.left)
			if cur.right:
				queue.append(cur.right)
				
		return res
				
