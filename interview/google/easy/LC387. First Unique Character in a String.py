"""

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""
from collections import defaultdict
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = defaultdict(lambda: 0)
        for c in s:
            m[c] += 1
        for i, c in enumerate(s):
            if m[c] == 1:
                return i
        return -1