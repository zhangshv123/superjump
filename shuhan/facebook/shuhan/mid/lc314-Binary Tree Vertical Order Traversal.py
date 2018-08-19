#!/usr/bin/python
from collections import defaultdict
from collections import deque
class Solution(object):
	class Solution(object):
	def verticalOrder(self, root):
		res = []
		if not root:
			return res
		d = defaultdict(list)
		q = deque()
		q.append((root, 0))
		while len(q) > 0:
			size = len(q)
			for i in range(size):
				cur,idx = q.popleft()
				d[idx].append(cur.val)
				if cur.left:
					q.append((cur.left, idx-1))
				if cur.right:
					q.append((cur.right, idx+1))
		keys = sorted(d.keys())
		for key in keys:
			res.append(d[key])
		return res

