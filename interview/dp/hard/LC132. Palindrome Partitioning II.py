递推方程
dp[i]代表前i个char最小的cut数
dp[i] = min(dp[k])+1   0<k<i if s[k:i] isPalindrome
or 0 if s[:i+1] is palindrome
import sys
class Solution(object):
	def minCut(self, s):
		dp = [0]* (len(s)+1)
		pds = self.isPalindrome(s)
		dp[0] = 0
		# dp[i] is the min cut for the first i chars of S.
		for i in range(1, len(s)+1): # 0..i-1
			if pds[0][i-1]:
				dp[i] = 0
				continue
			dp[i] = i
			for k in range(1, i): # subcase of the first k chars (0<k<i)
				if pds[k][i-1]: # could improve to O(1) if we precalcute palindrome(i, j)
					dp[i] = min(dp[k]+1, dp[i])
		return dp[-1]
	
递推方程：
dp[i][j]:代表s[i]到s[j](包括s[j])是否是一个palindrome
初始化 dp[i][i] = true 
dp[i][i+1] = s[i] == s[i+1]
dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
			
	def isPalindrome(self, s):
			size = len(s)
			dp = [[None for _ in range(size)] for _ in range(size)] 
			for i in range(size):
				dp[i][i] = True
				if i < size - 1:
					dp[i][i+1] = s[i] == s[i+1]
			for i in range(size):
				for j in range(i):
					if dp[j][i] != None:
						continue
					else:
						dp[j][i] = s[i] == s[j] and dp[j+1][i-1]
	#				print i,j,dp[i][j]
			
			return dp
#	def isPalindrome(self, s):
#		size = len(s)
#		dp = [[False for _ in range(size)] for _ in range(size)] 
#		for i in range(size):
#			dp[i][i] = True
#			if i < size - 1:
#				dp[i][i+1] = s[i] == s[i+1]
#		for i in range(size):
#			for j in range(0,i):
#				dp[j][i] = s[i] == s[j] and dp[j+1][i-1]
#	#				print i,j,dp[i][j]
#			
#		return dp[0][size-1]


s = Solution()
print s.minCut("aab")
print s.minCut("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
		
