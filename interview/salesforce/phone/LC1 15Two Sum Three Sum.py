"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}
        for i, num in enumerate(nums):
            if target - num in m:
                return [m[target - num], i]
            m[num] = i
        return [-1, -1]

"""
three sums
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                if j != i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                elif k != len(nums) - 1 and nums[k] == nums[k + 1]:
                    k -= 1
                else:
                    total = nums[i] + nums[j] + nums[k] 
                    if total == 0:
                        res.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                    elif total < 0:
                        j += 1
                    else:
                        k -= 1
        return res        