"""
（1）一个n*n棋盘，求从左上角到右上角的所有路径个数。每次移动时，只能向右一格、向右上一格、或向右下一格。
follow up：又给了若干指定必须经过的格子，求路径数目。
dropbox也问过类似问题，格子走法一样，问的是：棋盘里每个格子上都有一个数字，求从左边沿任何一个格子出发到右边沿任何一个格子结束的所有路径中，沿途值之和最小的那个路径的值。
"""
class Solution:
	def paths(self, M, N, ll):
		def uniquePaths(p1, p2):
			"""
			:type m: int
			:type n: int
			:rtype: int
			"""
			m, n = abs(p1[0] -p2[0]) + 1, abs(p1[1] - p2[1]) + 1
			dp = [[0 for j in range(n)] for i in range(M)]
			dp[p1[0]][0] = 1
			for j in range(n):
				for i in range(M):
					if j - 1 >= 0:
						dp[i][j] += dp[i][j - 1]
						if i - 1 >= 0:
							dp[i][j] += dp[i - 1][j - 1]
						if i + 1 < M:
							dp[i][j] += dp[i + 1][j - 1]
			print dp
			return dp[m - 1][n - 1]
		res = 1
		ll.insert(0, (0, 0))
		ll.append((0, N - 1))
		print ll
		for i in range(len(ll) - 1):
			print res
			res *= uniquePaths(ll[i], ll[i + 1])
		return res
s = Solution()
print s.paths(2, 2, [(1, 1)])