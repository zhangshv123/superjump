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
			if dw[str[i]] != char or dc[char] != str[i]: #第14行
				return False
		return True

或者一个dictionary的方法：
class Solution(object):
	def wordPattern(self, pattern, str):
		d = dict()
		str = str.split(" ")

		if len(pattern) != len(str):
			return False

		for i,char in enumerate(pattern):
			if char in d:
				if d[char] != str[i]:
					return False
			else:
				if str[i] in d.values(): #value已经存在了，说明是其他p放进来的，错！
					return False
				d[char] = str[i] #说明key不在d，value也不在d，就直接加进去
		return True


s = Solution()
print s.wordPattern("abba", "dog dog dog dog")
print s.wordPattern("abba", "dog cat cat dog")
print s.wordPattern("aaaa", "dog cat cat dog")
print s.wordPattern("ab", "dog dog")
				