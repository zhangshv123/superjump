# 给一个数字字母的Map， a --1, b --2, ... z --26。现在给一个数字string,  要decode成字母，输出所有可能结果。dfs + memrization， 问了复杂
def decodeString(s):
	m = {}
	for i in range(26):
		m[str(i + 1)] = chr(ord('a') + i)
	dp = {}
	def dfs(s):
		if len(s) == 0:
			return ['']
		if s in dp:
			return dp[s]
		res = []
		if s[0] in m:
			for ans in dfs(s[1:]):
				res.append(m[s[0]] + ans)
		if len(s) > 1 and s[:2] in m:
			for ans in dfs(s[2:]):
				res.append(m[s[:2]] + ans)
		dp[s] = res				
		return dp[s]
	return dfs(s)
print(decodeString("203"))