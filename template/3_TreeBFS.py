"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
		3
	 / \
	9  20
		/  \
	 15   7
return its level order traversal as:
[
	[3],
	[9,20],
	[15,7]
]
"""
from collections import deque
class Solution(object):
	def levelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		if not root:
			return []
		res = []
		q = deque()
		q.append(root)
		while len(q) > 0:
			layer = []
			size = len(q) #如果不需要一层一层的，那就不需要第40，41行
			for i in range(size):
				cur = q.popleft()
				layer.append(cur.val)
				if cur.left:
					q.append(cur.left)
				if cur.right:
					q.append(cur.right)
			res.append(layer)
		return res

图的BFS和树的有点不同，图的需要一个set，因为图可能有环
图的标准BFS 参照Clone Graph 那道题的getNodes方法：
http://tinyurl.com/yddsx7qc