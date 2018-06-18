"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.
"""
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [sys.maxint for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if i + coin <= amount:
                    dp[i + coin] = min(dp[i + coin], dp[i] + 1)
        return dp[amount] if dp[amount] != sys.maxint else -1


#要是单纯问 有多少种可以组成amount的方法：
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int
        :type amount: int
        :rtype: int
        """
        res = []
        path = []
        self.helper(amount, coins, 0 , res, path)
        print res
        return len(res)
        
    def helper(self, target, coins, idx, res, path):
        if target == 0:
            if path not in res:
                res.append(path[:])
                return
        for i in range(idx, len(coins)):
            if coins[i] > target:
                return
            path.append(coins[i])   # The reference of path is not changed!
            self.helper(target-coins[i], coins, i, res, path)
            path.pop()
        
s = Solution()
print s.coinChange([1,2,5], 11)