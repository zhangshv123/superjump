#!/usr/bin/python
"""
Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
    [3],
    [1],
    [2],
    [1,2,3],
    [1,3],
    [2,3],
    [1,2],
    []
]
"""

"""
sol1: every item can appear or not
[]
[][1]
[][1] + [2][1 2]
[][1][2][1 2] + [3][1 3][2 3][1 2 3] 
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            size = len(res)
            for i in range(size):
                res.append(res[i] + [num])
        return res

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = [[]]
        for num in nums:
            new_subsets = map(lambda a: a + [num], subsets)
            subsets += new_subsets
        return subsets

"""
recursion
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, path = [], []
        nums.sort()
        self.dfs(0, nums, res, path)
        return res
    
    def dfs(self, index, nums, res, path):
        res.append(path[:])#这里只是copy了path的值给另外一个新的object，这个object和path无关
        for i in range(index, len(nums)):
            path.append(nums[i])
            self.dfs(i + 1, nums, res, path)
            path.pop()
"""
path:
1
1 2
1 2 3
1 2
1 3
2 3
2
3





res:
[], [1], [1,2], [1,2,3], [1, 3], [2], [2,3], [3]
"""

"""
iteration
sol3: use bit represent ele appear or not, pow(2, len(nums)) sol
each bit string represet one subset
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        subsets = []
        for i in range(pow(2, length)):
            subset = []
            for j in range(length):
                if i >> j & 1:
                    subset.append(nums[j])
            subsets.append(subset)
        return subsets
"""
iteration
subset 2
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
                #如果和上一个重复，把前一个的size以后的元素提取， append
                if i == 0 or nums[i] != nums[i -1] or j>= pre_size:
                    res.append(res[j] + [nums[i]])
            pre_size = size
        return res


"""
recursion
"""
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
             """
            上面这一连串判断条件，重点在于要能理解!used(i-1) 
            要理解这个，首先要明白i作为数组内序号，i是唯一的 
            给出一个排好序的数组，[1,2,2] 
            第一层递归            第二层递归            第三层递归 
            [1]                    [1,2]                [1,2,2] 
            序号:[0]                 [0,1]            [0,1,2] 
            这种都是OK的，但当第二层递归i扫到的是第二个"2"，情况就不一样了 
            [1]                    [1,2]                [1,2,2]             
            序号:[0]                [0,2]                [0,2,1] 
            所以这边判断的时候!used(0)就变成了true，不会再继续递归下去，跳出循环 
            步主要就是为了去除连续重复存在的，很神奇反正 = =|| 
            """
            if i > index and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            self.dfs(i + 1, nums, res, path)
            path.remove(nums[i])   
