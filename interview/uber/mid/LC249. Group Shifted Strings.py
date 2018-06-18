"""
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". 
We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"], 
A solution is:

[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
"""

from collections import defaultdict
class Solution(object):
	def getKey(self, s):
		if len(s) == 0:
			return s
		shift = ord(s[0]) - ord('a')
		return "".join(map(lambda a: chr((ord(a) - shift - ord('a')) % 26 + ord('a')), s))
	
	def groupStrings(self, strings):
		"""
		:type strings: List[str]
		:rtype: List[List[str]]
		"""
		m = defaultdict(list)
		for s in strings:
			m[self.getKey(s)].append(s)
		return m.values()