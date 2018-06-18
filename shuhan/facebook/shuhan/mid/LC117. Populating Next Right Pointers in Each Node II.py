#!/usr/bin/python
from collections import deque
#BFS比DFS和TOPDOWN都简单！
class Solution:
	# @param root, a tree link node
	# @return nothing
	def connect(self, root):
		if not root:
			return 
		queue = deque()
		queue.append(root)
		while queue:
			size = len(queue)
			for i in range(size):
				cur = queue.popleft()
				if i < size-1:
					cur.next = queue[0]
				if cur.left:
					queue.append(cur.left)
				if cur.right:
					queue.append(cur.right)
