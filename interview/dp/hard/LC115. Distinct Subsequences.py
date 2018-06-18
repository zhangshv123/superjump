"""
Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
"""
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        #dp[i][j]: s[:i], t[:j]子问题
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if j == 0:
                    dp[i][j] = 1
                elif i == 0 and j != 0:
                    dp[i][j] = 0
                else:
                    if s[i - 1] != t[j - 1]:
                        dp[i][j] = dp[i - 1][j]
                    else:
                        #用最后一位|不用最后一位 s[i - 1]
                        dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
        return dp[m][n]
#滚动数组
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        #dp[i][j]: s[:i], t[:j]子问题
        dp = [0 for _ in range(n + 1)]
        for i in range(m + 1):
            #reverse order, so [i-1][j-1] won't be overwriten by [i][j-1] first
            for j in reversed(range(n + 1)):
                if j == 0:
                    dp[j] = 1
                elif i == 0 and j != 0:
                    dp[j] = 0
                else:
                    if s[i - 1] == t[j - 1]:
                        dp[j] += dp[j - 1]
        return dp[n]        