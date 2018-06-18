dp[i][j] 代表s的第i位和p的第j位是否match，返回boolean
分为3种基本情况：
1) "C"字母： 这种最简单，直接看i和j是否相同&&之前是否match:s[i]==p[j]&&dp[i-1]dp[j-1]
2) ".": 这种也简单，因为.可以代表任何字母，所以肯定是match的，直接看dp[i-1][j-1]
3) "*":这种最复杂，还要分为3种情况：
{
	"":代表0个，这时候就看dp[i][j-2]
	"C":代表一个，这时候就看dp[i-1][j-2]
	"CCC":代表K个，这时候就看dp[i-k][j-2],并且k<=i
}
class Solution(object):
	def isMatch(self, s, p):
		#i:s, j:p
		len_s, len_p = len(s), len(p)
		#initilize dp
		#dp index is 1 more than string index dp[0][0]: ""~""
		dp = [[ False for i in range(len_s + 1)] for j in range(len_p + 1)] #p行i列
		dp[0][0] = True
		for j in range(2, len_p + 1): #basecase:当s[0]=""那p一定会match
			if p[j - 1] == "*":   
				dp[j][0] = dp[j - 2][0]
		for j in range(1, len_p + 1):
			for i in range(1, len_s + 1):
				if p[j - 1] == "*": #最复杂的情况
					k = 0
					while k <= i: 
						dp[j][i] |= dp[j-2][i - k]
						if p[j - 1 - 1] != "." and s[i - 1 - k] != p[j - 1 - 1]:
							break
						k += 1
				elif p[j - 1] == ".":
					dp[j][i] = dp[j-1][i-1] #当j是'.'的时候
				else:
					dp[j][i] = dp[j-1][i-1] and p[j - 1] == s[i - 1] #当j是字母不是特殊符号
		return dp[len_p][len_s]