game thoery:
	如果B不能必胜，那么A一定可以必胜，反之亦然
dfs的定义：
dfs(n,visited,target)
从N - visited 当中选择，当前玩家是否必胜
main function:
	return dfs(N,[],M)

from collections import defaultdict
class Solution(object):
	def canIWin(self, N, M):
		visited = defaultdict(lambda: False)
		return self.dfs(N,visited,M)
	
	def dfs(self, n, visited, target): #代表当前选手在 N-visited 之中，选一个数，一定会必胜
		for c in range(1,n+1):
			if visited[c] == True:
				continue
			if c >= target:
				return True
			visited[c] = True
			local = self.dfs(n, visited, target - c) #如果local是false只能说明我的选择不好
			visited[c] = False
			if not local:
				return True
		return False

			
			
