"""
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
"""
"""
f(i, j) := minimum cost (or steps) required to convert first i characters of word1 to first j characters of word2
这里是前i个和前j个，为了代码便于初始化而已

Case 1: word1[i] == word2[j], i.e. the ith the jth character matches.

f(i, j) = f(i - 1, j - 1)
Case 2: word1[i] != word2[j], then we must either insert, delete or replace, whichever is cheaper

f(i, j) = 1 + min { f(i, j - 1), f(i - 1, j), f(i - 1, j - 1) }
f(i, j - 1) represents insert operation
f(i - 1, j) represents delete operation
f(i - 1, j - 1) represents replace operation
"""
#bottom-up translation of this recurrent relation
转移方程是：
dp[i][j] = 三个之中找最小值 min(
    dp[i-1][j] + 1, delete
    dp[i][j-1] + 1, insert
    dp[i-1][j-1] if word1[i] == word2[j] 如果不等 dp[i-1][j-1]+1) replace

import sys
class Solution(object):
    def minDistance(self, word1, word2):
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)] #这里初始化为0，初始化为任何数都可以！
        dp[0][0] = 0
        for j in range(len(word2) + 1):
            dp[0][j] = j
        for i in range(len(word1) + 1):
            dp[i][0] = i
        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j-1]+1
                
                dp[i][j] = min(dp[i][j-1]+1,dp[i-1][j]+1,dp[i][j])
        return dp[-1][-1]

#滚动数组        
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        if m == 0 or n == 0:
            return max(m, n)
        #dp[i][j]: word1[:i], word2[:j] 子问题
        dp = [[sys.maxint for _ in range(n + 1)] for _ in range(2)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i % 2][j] = i
                else:
                    if word1[i - 1] == word2[j - 1]:
                        dp[i % 2][j] = dp[(i - 1)% 2][j - 1]
                    else:
                        dp[i % 2][j] = min(dp[(i - 1) % 2][j - 1], dp[(i - 1) % 2][j], dp[i % 2][j - 1]) + 1
        return dp[m % 2][n]        
#backtracing
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        if m == 0 or n == 0:
            return max(m, n)
        #dp[i][j]: word1[:i], word2[:j] 子问题
        dp = [[sys.maxint for _ in range(n + 1)] for _ in range(m + 1)]
        def helper(i, j):
            if i == 0 or j == 0:
                return max(i, j)
            if dp[i][j] != sys.maxint:
                return dp[i][j]
            res = sys.maxint
            if word1[i - 1] == word2[j - 1]:
                res = helper(i - 1, j - 1)
            else:
                res = min(helper(i - 1, j - 1), helper(i - 1, j), helper(i, j - 1)) + 1
            dp[i][j] = res
            return res
        return helper(m, n)        