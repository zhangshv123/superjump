#!/usr/bin/python
"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
please remember always give naive solution first, otherwise might be regarded as cheating , like count..
"""
class Solution(object):
    def swap(self, i, j, nums):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        r, w, b = 0, 0, len(nums) - 1
        while w <= b:
            if nums[w] == 1:
                w += 1
            elif nums[w] == 0:
                self.swap(w, r, nums)
                w += 1
                r += 1
            else:
                self.swap(w, b, nums)
                b -= 1
                
s = Solution()
nums = [1,0]
s.sortColors(nums)
print nums