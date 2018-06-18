"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
"""

class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        p = [[False for _ in range(N)] for _ in range(N)]
        for i in range(N):
            p[i][i] = True
        for i in range(N - 1):
            if s[i] == s[i + 1]:
                p[i][i + 1] = True
        for gap in range(2, N):
            for i in range(N - gap):
                j = i + gap
                p[i][j] = p[i + 1][j - 1] and s[i] == s[j]
        return sum(map(lambda a: sum(a), p))

# Idea is start from each index and try to extend palindrome for both odd and even length.
class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        def getCount(i, j):
            count = 0
            while i >= 0 and j < N and s[i] == s[j]:
                count += 1
                i -= 1
                j += 1
            return count
        return sum(map(lambda i: getCount(i, i) + getCount(i, i + 1), range(N)))        
                