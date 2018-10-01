#思路：
#dp[i][j]代表从i开始到j结尾，包含i,j的substring是否是panlidrome!
class Solution(object):
	def longestPalindrome(self, s):
		res = 1
		n = len(s)
		dp = [[False for i in range(n)] for j in range(n)]
		for i in range(n):
			dp[i][i] = True
		for i in range(n):
			for j in range(i):
				dp[i][j] = True
		for l in range(1, n+1):
			for i in range(n-l+1):
				j = i + l - 1
				if i == j:
					continue
				if s[i] == s[j] and dp[i+1][j-1]:
					dp[i][j] = True
					res = max(res, j-i+1)
		return res
		
s = Solution()
print s.longestPalindrome("ababa")
				
		