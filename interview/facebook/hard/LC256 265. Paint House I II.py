"""
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. 
The cost of painting each house with a certain color is different. You have to paint all the houses such 
that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, 
costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 
with color green, and so on... Find the minimum cost to paint all houses.
"""
"""
思路: 一道很明显的动态规划的题目. 每个房子有三种染色方案, 那么如果当前房子染红色的话, 最小代价将是上一个房子的绿色和蓝色的
最小代价+当前房子染红色的代价. 对另外两种颜色也是如此. 因此动态转移方程为: 
             dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i-1][0];
             dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i-1][1];
             dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i-1][2];
"""

class Solution(object):
    def minCost(self, costs):
        if len(costs) == 0:
            return 0
        n = len(costs)
        dp = [[0 for _ in range(3)] for _ in range(n + 1)]
        for i in range(1,n+1):
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i-1][0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i-1][1]
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i-1][2]
        return min(dp[n])

class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0:
            return 0
        n = len(costs)
        dp = [[0 for _ in range(3)] for _ in range(n)]
        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]
        for i in range(1, n):
            dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + costs[i][0]
            dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + costs[i][1]
            dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + costs[i][2]
        return min(dp[n-1])

#paint house II 
"""
To solve this DP problem:

If there’s no constraint, we choose min cost for each house.
Since house[i] and house[i - 1] cannot have the same color j, we should choose 2nd min color for house[i - 1].
If we choose the 3rd min color for house[i - 1], we might miss potential min cost.
min(i) = min(cost[i][j] + 1st min / 2nd min), 0 < j < n.
Since current row only relies on last row for getting mins and avoiding same color, O(1) space is enough.
"""
import sys
class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0:
            return 0
        min1, min2, index1 = 0, 0, -1
        for i in range(len(costs)):
            m1, m2, idx1 = sys.maxint, sys.maxint, -1
            for j in range(len(costs[0])):
                cost = costs[i][j] + (min1 if j != index1 else min2)
                if cost < m1:
                    m2, m1, idx1 = m1, cost, j
                elif cost < m2:
                    m2 = cost
            min1, min2, index1 = m1, m2, idx1
        return min1





"""
There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each
 house with a certain color is different. You have to paint all the houses such that no two adjacent houses
  have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, 
costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with
 color 2, and so on... Find the minimum cost to paint all houses.
"""
class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0 or len(costs[0]) == 0:
            return 0
        n = len(costs)
        k = len(costs[0])
        #if only one color
        if k == 1:
            return sum(map(lambda house: house[0],costs))
        dp = [[sys.maxint for _ in range(k)] for _ in range(n)]
        #dp function
        for i in range(n):
            for j in range(k):
                if i == 0:
                    dp[i][j] = costs[i][j]
                else:
                    dp[i][j] = sys.maxint
                    for l in range(k):
                        if l != j:
                            dp[i][j] = min(dp[i][j], costs[i][j] + dp[i - 1][l])
        return min(dp[n - 1])

#滚动数组
class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0 or len(costs[0]) == 0:
            return 0
        n = len(costs)
        k = len(costs[0])
        #if only one color
        if k == 1:
            return sum(map(lambda house: house[0],costs))
        dp = [[sys.maxint for _ in range(k)] for _ in range(2)]
        #dp function
        for i in range(n):
            for j in range(k):
                if i == 0:
                    dp[i % 2][j] = costs[i][j]
                else:
                    dp[i % 2][j] = sys.maxint
                    for l in range(k):
                        if l != j:
                            dp[i % 2][j] = min(dp[i % 2][j], costs[i][j] + dp[(i - 1) % 2][l])
        return min(dp[(n - 1) % 2])        