思路：
max_v代表最长的数字，
res返回最长的回文substring
dp[i][j]代表包含i,j的substring是否为回文串，值是true和false
时间复杂度0（n平方）
如果用prefix tree可能是做到0(n)
推到公式是:
	dp[i][i]是true
	dp[i][k]是true，这里k<i
	如果s[i] == s[j]并且dp[i+1][j-1]是一个回文串(true):
		dp[i][j] = True
		并且可以看当前是不是最长，update res 和max_v
	
class Solution(object):
	def longestPalindrome(self, s):
		res = ""
		max_v = 0
		n = len(s)
		if n <= 1:
			return s
		dp = [[False for i in range(n)] for j in range(n)]
		for i in range(n):
			dp[i][i] = True
			res = s[i]
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
					if j - i + 1 > max_v:
						max_v = max(max_v, j-i+1)
						res = s[i:j+1]
		return res
		
s = Solution()
print s.longestPalindrome("ccacc")
				
		