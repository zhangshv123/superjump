game thoery:
	如果B不能必胜，那么A一定可以必胜，反之亦然
dfs的定义：
dfs(n,visited,target)
从N - visited 当中选择，当前玩家是否必胜
main function:
	return dfs(N,[],M)

时间复杂度：
从N^N（排列) 优化到2^N(组合)

from collections import defaultdict
class Solution(object):
	def canIWin(self, N, M):
		total = (1+N)*N/2
		if total < M:
			return False
		visited = 0
		d = dict()
		return self.dfs(N, visited, M, d)
	
	def dfs(self, n, visited, target, d):
		for c in range(1,n+1):
#			if visited[c] == 1:
			if visited&(1<<c) != 0:
				continue
			if c >= target:
				return True
#			visited[c] = True
			visited = visited^(1<<c)
			if visited in d:
				local = d[visited]
			else: 
				local = self.dfs(n, visited, target - c, d)
				d[visited] = local
			visited = visited^(1<<c)
			if not local:
				return True
		return False

s = Solution()
print s.canIWin(18, 79)
print s.canIWin(10, 11)
			
			
