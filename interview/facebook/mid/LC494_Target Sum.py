#!/usr/bin/python
"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
http://www.cnblogs.com/grandyang/p/6395843.html
"""
from collections import defaultdict
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]
        dp[0][0] = 1
        for i in range(1, len(nums) + 1):
            for value, time in dp[i-1].items():
                dp[i][value - nums[i-1]] += time
                dp[i][value + nums[i-1]] += time
        return dp[len(nums)][S]