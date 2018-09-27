思路：
最简单的模式，把2边都翻译成一种语言，然后看是否一样就可以了
比如把"abba"翻译成list1 = [1221]，然后把"dog cat cat dog"也翻译成list2 = [1221]，最后看list1 == list2就好！
class Solution(object):
	def wordPattern(self, pattern, str):
		str = str.split(" ")
		if len(pattern) != len(str):
			return False
		dc, dw = dict(), dict()
		count = 0
		list1 = []
		for c in pattern:
			if c not in dc:
				dc[c] = count
				list1.append(count)
				count += 1
			else:
				list1.append(dc[c])
		count = 0
		list2 = []
		for word in str:
			if word not in dw:
				dw[word] = count
				list2.append(count)
				count += 1
			else:
				list2.append(dw[word])
		return list1 == list2
或者和LC205一样做的做法：
class Solution(object):
	def wordPattern(self, s, str):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		t = str.split(" ")
		if len(s) != len(t):
			return False
		replace_map = {}
		for i in range(len(s)):
			if s[i] not in replace_map:
				replace_map[s[i]] = t[i]
			else:
				if replace_map[s[i]] != t[i]:
					return False
		values = replace_map.values()
		return len(set(values)) == len(values)

s = Solution()
print s.wordPattern("abba", "dog dog dog dog")
print s.wordPattern("abba", "dog cat cat dog")
print s.wordPattern("aaaa", "dog cat cat dog")
print s.wordPattern("ab", "dog dog")
				