#!/usr/bin/python
class Solution(object):
	def groupAnagrams(self, strs):
		"""
		:type strs: List[str]
		:rtype: List[List[str]]
		"""
		d = dict()
		for word in strs:
			cur = ''.join(sorted(word)) 
#		注意这里是用sorted就不会改变原本的word！
			if cur in d:
				d[cur].append(word)
			else:
				d[cur] = [word]
		return d.values()
s = Solution()
print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])