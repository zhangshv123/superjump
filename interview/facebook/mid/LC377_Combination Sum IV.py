#!/usr/bin/python
"""
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
"""
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0 for _ in range(target + 1)]
        for i in range(target + 1):
            if i in nums:
                dp[i] += 1
            for num in filter(lambda a: a < i, nums):
                dp[i] += dp[i - num]
        return dp[target]
s = Solution()
print s.combinationSum4([1, 2, 3], 4)