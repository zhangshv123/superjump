"""
Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.
"""
import sets
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = set()
        for c in s:
            if c in d:
                d.remove(c)
            else:
                d.add(c)
        return len(d) < 2