game thoery:
	如果B不能必胜，那么A一定可以必胜，反之亦然
dfs的定义：
dfs(n,visited,target)
从N - visited 当中选择，当前玩家是否必胜
main function:
	return dfs(N,[],M)

from sets import Set
class Solution(object):
	def canIWin(self, N, M):
		return dfs(n,(),target)
	
	def dfs(self, n, visited, target):
		for c in n:
			if c not in visited:
				if c >= target:
					return True
			visited.add(c)
			local = self.dfs(n, visited, target - c)
			if not local:
				return True
			visited.remove(c)
		return False

			
			
