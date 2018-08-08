解题思路：
A必胜-》B必败
for 所有可能：
   if B 必败：
      A必胜
	  return True
return False
class Solution(object):
	def canWin(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		return self.helper(s)
		
		
	def helper(self, s):
		idx = 0
		while idx + 1 < len(s):
			if s[idx:idx+2] == "++":
				tmp = s[:idx] + "--" + s[idx+2:]
				if not self.helper(tmp):
					return True
			idx += 1
		return False
s = Solution()
print s.canWin("----")