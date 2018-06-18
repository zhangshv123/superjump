#!/usr/bin/python
class Solution(object):
	def isOneEditDistance(self, s, t):
		if s == t:
			return False
		if len(s) == len(t):
			return self.isOneCharacterReplaced(s,t)
		str_s = t if len(s) > len(t) else s
		str_t = s if len(s) > len(t) else t
		return self.isOneCharacterAdded(str_s,str_t)
		
	def isOneCharacterReplaced(self, s, t):
		count = 0
		for i in range(len(s)):
			if s[i] != t[i]:
				count +=1
		if count !=1:
			return False
		return True
		
	def isOneCharacterAdded(self, str_s, str_t):
		count, i, j = 0, 0, 0
		while j < len(str_t):
#			大和小的比，都是移动大的那个指针，小的只有相等的时候才移动
			if i >= len(str_s) or str_s[i] !=str_t[j]:
				count += 1
				j += 1
			else:
				i += 1
				j += 1
		return count == 1
