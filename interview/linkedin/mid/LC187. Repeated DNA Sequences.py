class Solution(object):
	def findRepeatedDnaSequences(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		seen,repeated = set(),set()
		for i in range(len(s)-9):
			ten = s[i:i+10]
			if ten in seen:
				repeated.add(ten)
			else:
				seen.add(ten)
		
		return list(repeated)
s = Solution()
print s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")