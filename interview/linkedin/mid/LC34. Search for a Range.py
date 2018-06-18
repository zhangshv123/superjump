"""
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""
#九章模板
class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchFirst(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start+1 < end:
            mid = start + (end - start) / 2
            if target == nums[mid]:
                end = mid
            elif target < nums[mid]:
                end = mid
            else:
                start = mid
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1
            
    def searchLast(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start+1 < end:
            mid = start + (end - start) / 2
            if target == nums[mid]:
                start = mid
            elif target < nums[mid]:
                end = mid
            else:
                start = mid
        if nums[end] == target:
            return end
        elif nums[start] == target:
            return start
        else:
            return -1
            
    def searchRange(self, A, target):
        # write your code here
        if not A:
            return [-1,-1]
        return [self.searchFirst(A,target),self.searchLast(A,target)]
#豆豆version
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