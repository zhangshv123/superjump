思路：这道题超无聊，因为安卓机有一种特殊技术，就是比如1->6，不会经过2和5
connector[i][j]代表从i走到j要走的额外的格子idex，比如1-3要经过格子2
剩下的就是传统的DFS了！
class Solution(object):
	def numberOfPatterns(self, m, n):
		"""
		:type m: int
		:type n: int
		:rtype: int
		"""
		res = []
		connector =[[0 for i in range(10)] for j in range(10)]
		connector[1][3] = connector[3][1] = 2
		connector[1][7] = connector[7][1] = 4
		connector[3][9] = connector[9][3] = 6
		connector[9][7] = connector[7][9] = 8
		connector[1][9] = connector[9][1] = 5
		connector[3][7] = connector[7][3] = 5
		connector[2][8] = connector[8][2] = 5
		connector[4][6] = connector[6][4] = 5
		for i in range(1,10):
			self.dfs([i], res, connector, m, n)
		return len(res)
	
	def dfs(self, path, res, d, m, n):
		if len(path) >= m and len(path) <= n:
			res.append(path[:])
			
		if len(path) > n:
			return
		
		for j in range(1,10):
			if j in path:
				continue
			if d[path[-1]][j] == 0 or d[path[-1]][j] in path:
				path.append(j)
				self.dfs(path, res, d, m, n)
				path.pop()

s = Solution()
print s.numberOfPatterns(3, 4)
		