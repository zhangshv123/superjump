"""
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?
"""
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m, n = len(s), len(t)
        dp = [False for _ in range(m + 1)]
        for j in range(n + 1):
            for i in reversed(range(m + 1)):
                #base
                if i == 0 and j == 0:
                    dp[i] = True
                elif i == 0 and j <= n:
                    dp[i] = True
                elif i != 0 and j == 0:
                    dp[i] = False
                else:
                    if s[i - 1] == t[j - 1]:
                        dp[i] = dp[i - 1]
        return dp[m]