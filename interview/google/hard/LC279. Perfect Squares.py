"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
"""
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidates = [i * i for i in range(1, int(math.sqrt(n)) + 1)]
        dp = [sys.maxint for _ in range(n + 1)]
        dp[0] = 0
        for i in range(n):
            if dp[i] == sys.maxint:
                continue
            for cal in candidates:
                if cal + i > n:
                    break
                dp[cal + i] = min(dp[cal + i], dp[i] + 1)
        return dp[n]


import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidates = [i * i for i in reversed(range(1, int(math.sqrt(n)) + 1))]
        q = [n]
        idx, level, preSize, size = 0, 0, 0, 0
        while idx < len(q):
            preSize = size
            size = len(q)
            level += 1
            for _ in range(size - preSize):
                val = q[idx]
                idx += 1
                for cal in candidates:
                    if cal == val:
                        return level
                    if cal > val:
                        continue
                    if val - cal in q:
                        continue
                    q.append(val - cal)
            
