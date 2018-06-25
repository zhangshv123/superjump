递推方程非常类似edit distance
dp[i][j] = true 代表s的前i个字母和p的前j分字母匹配成功
递推方程请看思路图
这里说说初始化
如果可以不用planB(前N个)就不用，但是这里如果不用就很难初始化，所以还是采用plan B
dp[0][j] = True if P[0..j-1] all "*" otherwise False
dp[i][0] = False
dp[0][0] = True
class Solution(object):
	def isMatch(self, s, p):
		dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
		dp[0][0] = True
		for j in range(1,len(p)+1):
			f = True
			for k in range(j):
				if p[k] != "*":
					f = False
					break
			dp[0][j] = f
		
		for i in range(1,len(s)+1):
			for j in range(1,len(p)+1):
				if (dp[i-1][j] or dp[i][j-1]) and p[j-1] == "*":
					dp[i][j] = True
				elif dp[i-1][j-1] and (p[j-1] == "?" or p[j-1] == s[i-1] or p[j-1] == "*"):
					dp[i][j] = True
		return dp[-1][-1]
s = Solution()
print s.isMatch("a", "a*")
