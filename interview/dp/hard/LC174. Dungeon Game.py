"""
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.


Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.
"""
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n = len(dungeon), len(dungeon[0])
        #dp[i][j]: start from (i, j), minimum health needs
        dp = [[sys.maxint for _ in range(n)] for _ in range(m)]
        dp[m - 1][n - 1] = max(1, 1 -dungeon[m - 1][n - 1])
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if i < m - 1:
                    dp[i][j] = min(dp[i][j], max(1, 1 - dungeon[i][j], dp[i + 1][j] - dungeon[i][j]))
                if j < n - 1:
                    dp[i][j] = min(dp[i][j], max(1, 1 - dungeon[i][j], dp[i][j + 1] - dungeon[i][j]))
        # print dp
        return max(1, dp[0][0])