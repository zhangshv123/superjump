#!/usr/bin/python
"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
    [-1, 0, 1],
    [-1, -1, 2]
]
"""
class Solution(object):
    def twoSum(self, start, nums, first_num):
        res_list = []
        i, j = start, len(nums) - 1
        while i < j:
            # skip duplicate, only use first
            if i > start and nums[i] == nums[i-1]:
                i += 1
                continue
            # skip duplicate, only use first
            if j < len(nums) - 1 and nums[j] == nums[j+1]:
                j -= 1
                continue
            if nums[i] + nums[j] < -first_num:
                i += 1
            elif nums[i] + nums[j] > -first_num:
                j -= 1
            else:
                res_list.append([first_num, nums[i], nums[j]])
                i += 1
                j -= 1
        return res_list
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sorted_nums = sorted(nums)
        res_list = []
        for i, first_num in enumerate(sorted_nums):
            # skip duplicate, only use first
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            res_list += self.twoSum(i + 1, sorted_nums, first_num)
        return res_list