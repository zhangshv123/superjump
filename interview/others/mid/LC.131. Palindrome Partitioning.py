"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]
"""
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.dfs(s, 0, [], res)
        return res
        
    def dfs(self, s, index, path, res):
        if index == len(s):
            res.append(path[:])
            return
        
        for i in range(index, len(s)):
            if self.isPalindrome(s[index:i+1]):
                path.append(s[index:i+1])
                self.dfs(s, i+1, path, res)
                path.pop()
        
    
    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        isPan = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            isPan[i][i] = True
        for i in range(n - 1):
            isPan[i][i + 1] = s[i] == s[i + 1]
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                isPan[i][i + length - 1] = isPan[i + 1][i + length - 2] and s[i] == s[i + length - 1]
        # dp[i] sub Problem of s[i:]
        dp = [[] for _ in range(n + 1)]
        dp[n].append([])
        for i in reversed(range(n)):
            for j in range(i, n + 1):
                if isPan[i][j - 1]: 
                    #word[i:j] + eachof f[j:]
                    dp[i] += map(lambda ans: [s[i: j]] + ans, dp[j])
        return dp[0]
        


class Solution(object):
    def helper(self, s, start, isPan, dp):
        if start == len(s):
            return [[]]
        if dp[start] != None:
            return dp[start]
        res = []
        for i in range(start, len(s)):
            if isPan[start][i]:
                res += map(lambda ans: [s[start: i+1]] + ans, self.helper(s, i + 1, isPan, dp))
        dp[start] = res
        return res
    
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        isPan = [[False for _ in range(n)] for _ in range(n)]
        dp = [None for _ in range(n)]
        for i in range(n):
            isPan[i][i] = True
        for i in range(n - 1):
            isPan[i][i + 1] = s[i] == s[i + 1]
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                isPan[i][i + length - 1] = isPan[i + 1][i + length - 2] and s[i] == s[i + length - 1]
        return self.helper(s, 0, isPan, dp)
        