#!/usr/bin/python
"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
    [2],
    [1],
    [1,2,2],
    [2,2],
    [1,2],
    []
]
"""
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        pre_size = 0
        nums.sort()
        for i in range(len(nums)):
            size = len(res)
            for j in range(size):
                if i == 0 or nums[i] != nums[i -1] or j>=pre_size:
                    res.append(res[j] + [nums[i]])
            pre_size = size
        return res


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, path = [], []
        nums.sort()
        self.dfs(0, nums, res, path)
        return res
    
    def dfs(self, index, nums, res, path):
        res.append(path[:])
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            self.dfs(i + 1, nums, res, path)
            path.remove(nums[i])   