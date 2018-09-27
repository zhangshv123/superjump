思路：用BFS
注意bi-party的定义！有些点是孤立的，那么它们在哪个party都可以
这里相当于涂色，把cur点涂成0，那么和它相连的点就是1
时间复杂度： O(n) 因为就是遍历
from collections import deque
class Solution(object):
	def isBipartite(self, graph):
		d = dict()
		visited = set()
		for i in range(len(graph)):
			if i not in visited:
				visited.add(i)
				if not self.bfs(i, graph, visited, d):
					return False
		return True
				
	def bfs(self, current, graph, visited, d):
		q = deque()
		q.append(current)
		d[current] = 0
		while len(q) > 0:
			size = len(q)
			for i in range(size):
				cur = q.popleft()
				for point in graph[cur]:
					if point in d: 
						if d[point] != abs(d[cur] - 1):
							return False
					else:
						d[point] = abs(d[cur] - 1)
						q.append(point)
						visited.add(point)
		return True

s = Solution()
print s.isBipartite([[1,3],[0,2],[1,3],[0,2]])
print s.isBipartite([[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]])
print s.isBipartite([[],[3],[],[1],[]])