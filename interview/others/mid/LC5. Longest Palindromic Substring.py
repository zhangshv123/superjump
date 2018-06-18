"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) == 0:
            return ""
        res = s[0]
        for i in range(len(s)):
            #even or odd
            for left, right in [(i - 1, i + 1), (i, i + 1)]:
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    if len(res) < right - left + 1:
                        res = s[left: right + 1]
                    left -= 1
                    right += 1
        return res
        
        