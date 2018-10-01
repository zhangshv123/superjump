思路：dp[i][j]代表不一定包含i或者j的，当前最长的回文长度
时间复杂度：N平方
推到公式是:
	dp[i][i] = 1
	如果s[i] == s[j]:
		dp[i][j] = dp[i+1][j-1] + 2
	不相等则：
		dp[i][j] = max(dp[i+1][j], dp[i][j-1])
class Solution(object):
	def longestPalindromeSubseq(self, s):
		n = len(s)
		if n <= 1:
			return n
		dp = [[0 for i in range(n)] for j in range(n)]
		for i in range(n):
			dp[i][i] = 1
		for l in range(1, n+1):
			for i in range(n-l+1):
				j = i + l - 1
				if i == j:
					continue #在这里不能直接赋值dp[i][i] = 1！
				if s[i] == s[j]:
					dp[i][j] = dp[i+1][j-1] + 2
				else:
					dp[i][j] = max(dp[i+1][j], dp[i][j-1])
		return dp[0][n-1]
		
s = Solution()
print s.longestPalindromeSubseq("a")