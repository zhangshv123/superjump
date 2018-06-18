"""
I
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
所有求substring，subarray， 最大最小都转化为以i为结尾的最大最小，
然后对于所有以i为最大最小的出的结论里遍历得到原问题的最大最小
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minp, maxgain = sys.maxint, 0     
        for p in prices:
            minp = min(p, minp)
            maxgain = max(maxgain, p - minp)
        return maxgain

"""
II
You may complete as many transactions as you like
"""        
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxgain = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                maxgain += prices[i] - prices[i - 1]
        return maxgain

"""
III
You may complete at most two transactions.
"""

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        minp, maxgain = prices[0], [0] * len(prices)     
        for i in range(1, len(prices)):
            minp = min(prices[i], minp)
            maxgain[i] = max(maxgain[i - 1], prices[i] - minp)
        maxp, maxgain1, maxtwo = prices[-1], [0] * len(prices), 0  
        for i in reversed(range(len(prices) - 1)):
            maxp = max(prices[i], maxp)
            maxgain1[i] = max(maxgain1[i + 1], maxp - prices[i])
            maxtwo = max(maxtwo, maxgain[i] + maxgain1[i])
        return maxtwo

