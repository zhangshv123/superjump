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
		print self.m
	def getParents(self, c):
		return self.m[c]
	def checkRelated(self, c1, c2):
		print self.m
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
	def printPath(self, c1, c2):
		res = []
		self.flight(c2, c1, [], res)
		return res
	def flight(self, c1, c2, path, res):
		if c1 in path:
			return
		path.append(c1)
		if c1 == c2:
			res.append(path[:])	
		else:
			for c in self.m[c1]:
				self.flight(c, c2, path, res)
		path.pop()		
s = Solution([("c1", "c2"), ("c2", "c3")])
print s.getParents("c3")
print s.printPath("c1", "c3")