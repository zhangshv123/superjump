"""
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7, 
A solution set is: 
[
  [7],
  [2, 2, 3]
]
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res, path = [], []
        def walk(start, t):
            if t == 0:
                res.append(path[:])
            if t > 0:
                for i in range(start, len(candidates)):
                    path.append(candidates[i])
                    walk(i, t - candidates[i])
                    path.pop()
        walk(0, target)
        return res
"""
follow up:
给的数组有重复乱序
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res, path = [], []
        def walk(start, t):
            if t == 0:
                res.append(path[:])
            if t > 0:
                for i, num in enumerate(candidates[start:]):
                    if i != start and candidates[i] == candidates[i - 1]:
                        continue
                    path.append(num)
                    walk(i + 1, t - num)
                    path.pop()
        walk(0, target)
        return res