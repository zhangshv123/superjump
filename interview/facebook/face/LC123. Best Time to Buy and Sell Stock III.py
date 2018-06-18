"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""
import sys
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        left, right = [0 for _ in range(n)], [0 for _ in range(n)]
        # m, g = min_so_far, max_profit_end_here 
        m, g = sys.maxint, 0
        for i, p in enumerate(prices):
            m = min(p, m)
            g = max(g, p - m)
            left[i] = g
        m, g = 0, 0
        for i, p in reversed(list(enumerate(prices))):
            m = max(p, m)
            g = max(g, m - p)
            right[i] = g
        res = 0
        for i in range(len(prices)):
            res = max(res, left[i] + right[i])
        return res