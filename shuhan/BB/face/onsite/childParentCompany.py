#!/usr/bin/python
"""
给我一堆列表，分别是子公司和母公司关系。写两个方法，一个是拿到一个给定公司的直接母公司。另外一个是判断给的两个公司是不是子母公司关系。
例子[(c1, c2), (c2, c3)]， 方法1:给c3， 返回c2；方法2:给c1和c3，返回true。
"""
from collections import defaultdict
from collections import deque
import sets
class Solution(object):
	def __init__(self, rs):
		self.m = defaultdict(set)
		for r in rs:
			self.m[r[1]].add(r[0])
	def getParents(self, c):
		return self.m[c]
	def checkRelated(self, c1, c2):
		q = deque()
		q.append(c2)
		visited = set()
		visited.add(c2)
		while len(q) > 0:
			cur = q.pop()
			for c in self.m[cur]:
				if c not in visited:
					visited.add(c)
					q.append(c)
					if c == c1:
						return True
		return False
s = Solution([("c1", "c2"), ("c2", "c3")])
print s.getParents("c3")
print s.checkRelated("c1", "c3")