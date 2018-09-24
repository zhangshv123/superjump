class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.children = {}

from collections import deque
class Solution(object):
	def compactTree(self, root, n):
		p,q = deque(), deque()
		p.append(root)
		
		while len(p) > 0:
			node = p.popleft()
			for child in node.children:
				p.append(node.children[child])
			node.children = {}
			
			if len(q) > 0:
				while len(q[0].children) >= n:
					q.popleft()
				q[0].children[node.val] = node
			q.append(node)
		return root	

root = TreeNode(1)
root.children[2] = TreeNode(2)
root.children[3] = TreeNode(3)
root.children[4]= TreeNode(4)
root.children[2].children[5] = TreeNode(5)
#root.right.left = TreeNode(6)
#root.right.right = TreeNode(7)

s = Solution()
print s.compactTree(root, 2) 			