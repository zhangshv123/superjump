#!/usr/bin/python
"""
Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
"""
"""
#双指针的题目完全可以用存在sol和不存在sol来分类
当存在sol，通过移动右指针找最优sol
当不存在sol，通过移动左指针达到sol
"""
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        subsum, left, right, min_length = 0, 0, 0, len(nums) + 1
        while right < len(nums):
            subsum += nums[right]
            while subsum >= s:
                min_length = min(min_length, right - left + 1)
                subsum -= nums[left]
                left += 1
            right += 1
        return min_length if min_length != len(nums) + 1 else 0