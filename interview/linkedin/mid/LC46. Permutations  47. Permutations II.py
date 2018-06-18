"""
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            size = len(res)
            new_res = []
            for i in range(size):
                subset = res[i]
                for j in range(len(subset) + 1): #对于插入的位置[1,2,3]就有4个插入的位置
                    new_subset = subset[:]
                    new_subset.insert(j, num)
                    new_res.append(new_subset)
            res = new_res
        return res

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        used = [False for _ in range(len(nums))]
        path, res = [], []
        self.dfs(used, nums, path, res)
        return res
        
    def dfs(self, used, nums, path, res):
        if len(path) == len(nums):
            res.append(path[:])
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            self.dfs(used, nums, path, res)
            path.pop()
            used[i] = False
"""
47 Given a collection of numbers that might contain duplicates
"""
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        used = [False for _ in range(len(nums))]
        path, res = [], []
        self.dfs(used, nums, path, res)
        return res
        
    def dfs(self, used, nums, path, res):
        if len(path) == len(nums):
            res.append(path[:])
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
        for i in range(len(nums)):
            if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                continue
            used[i] = True
            path.append(nums[i])
            self.dfs(used, nums, path, res)
            path.pop()
            used[i] = False

