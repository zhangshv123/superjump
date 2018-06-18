"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums) 
        dp = [False for _ in range(n)]
        dp[0] = True
        for i in range(n):
            if not dp[i]:
                continue
            for j in range(i + 1, min(i + nums[i] + 1, n)):
                dp[j] = True
        return dp[n - 1]


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums) 
        dp = [False for _ in range(n)]
        dp[0] = True
        for j in range(n):
            for i in range(j):
                dp[j] |= dp[i] and (nums[i] >= j - i)
                if dp[j]:
                    break
        return dp[n - 1]        