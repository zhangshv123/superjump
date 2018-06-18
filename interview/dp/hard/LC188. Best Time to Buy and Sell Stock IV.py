"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        #dp[i][k]: k transaction in i days(0 -> i - 1 )
        dp = [[0 for j in range(k + 1)] for i in range(n + 1)]
        for i in range(1, n):
            for j in range(1, k + 1):
                #base is 0 by default
                #not sell last day
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
                #sell last day
                for l in range(i):
                    dp[i][j] = max(dp[i][j], dp[l][j - 1] + prices[i] - prices[l])
        return dp[n - 1][k]
                    