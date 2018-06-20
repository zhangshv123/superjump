1.collect in-degree
2.put all nodes that indegree = 0 into queue
3.bfs
#返回 排好序的答案
from collections import defaultdict
from collections import deque
class Solution(object):
	def findOrder(self, numCourses, prerequisites):
		"""
		:type numCourses: int
		:type prerequisites: List[List[int]]
		:rtype: List[int]
		"""
		outDegreeMap = defaultdict(list)
		inDegreeNum = defaultdict(int)
		for pre in prerequisites:
			outDegreeMap[pre[1]].append(pre[0])
			inDegreeNum[pre[0]] += 1
		q = []
		for c in range(numCourses):
			if inDegreeNum[c] == 0:
				q.append(c)
		index = 0
		while index < len(q):
			cur = q[index]
			index += 1
			for c in outDegreeMap[cur]:
				inDegreeNum[c] -= 1
				if inDegreeNum[c] == 0:
					q.append(c)
		return q if len(q) == numCourses else []