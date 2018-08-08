class Solution(object):
	def generatePossibleNextMoves(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		res = []
		i = 0
		while i + 1 < len(s):
			if s[i:i+2] == "++":
				tmp = s[:i] + "--" + s[i+2:]
				res.append(tmp)
			i += 1
		return res

s = Solution()
print s.generatePossibleNextMoves("--")