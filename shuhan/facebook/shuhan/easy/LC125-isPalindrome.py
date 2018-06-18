#!/usr/bin/python
#或者reverse 一下整个s，然后比较rs和s是不是完全一样
class Solution(object):
	def isPalindrome(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		if s == None or len(s) == 0:
			return True
		head, tail = 0, len(s)-1
		s = s.lower()
		while head < tail:
			while not s[head].isalpha() and not s[head].isdigit() and head  < tail:
				head += 1
			while not s[tail].isalpha() and not s[tail].isdigit() and head < tail:
				tail -= 1
			if s[head] != s[tail]:
				return False
			else:
				head +=1
				tail -=1
		return True
		
s = Solution()
print s.isPalindrome("race a car")
