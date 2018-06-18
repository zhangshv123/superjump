"""
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1, -1]
        if nums == None or len(nums) == 0:
            return res
        left, right= 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if target <= nums[mid]:
                if nums[mid] == target:
                    res[0] = mid
                right = mid - 1
            else:
                left = mid + 1
        left, right= 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if target >= nums[mid]:
                if nums[mid] == target:
                    res[1] = mid
                left = mid + 1
            else:
                right = mid - 1
        return res

# 算法书版本
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = self.lower_bound(nums,target)
        end = self.upper_bound(nums,target)
        
        if start == -1 or nums[start] != target:
            return [-1, -1]
        elif end == -1: # start != -1
            return [start, len(nums) - 1]
        else: # start != -1 and end != -1
            return [start, end - 1]
        
    def lower_bound(self, nums, target):
        # the iterator of the value which is no less-than target.返回第一个大于等于target的位置
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) / 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        if start == len(nums):
            return -1
        else:
            return start
    
    def upper_bound(self, nums, target):
        # the iterator of the value which is greater then target.返回第一个完全大于target的位置
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) / 2
            if nums[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1
        if start == len(nums):
            return -1
        return start

nums = [1]
target = 1
s = Solution()
print s.searchRange(nums,target)