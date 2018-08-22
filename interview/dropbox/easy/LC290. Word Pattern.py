思路：
这道题超容易错！必须2边隐射好才可以，并且注意第14行，一定是if，不是elif，因为要马上检查！
class Solution(object):
	def wordPattern(self, pattern, str):
		dc, dw = dict(), dict()
		str = str.split(" ")
		if len(pattern) != len(str):
			return False
		for i,char in enumerate(pattern):
			if str[i] not in dw:
				dw[str[i]] = char
			if char not in dc:
				dc[char] = str[i]
			if dw[str[i]] != char or dc[char] != str[i]:
				return False
		return True

s = Solution()
print s.wordPattern("abba", "dog dog dog dog")
print s.wordPattern("abba", "dog cat cat dog")
print s.wordPattern("aaaa", "dog cat cat dog")
print s.wordPattern("ab", "dog dog")
				