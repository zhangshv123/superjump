#!/usr/bin/python
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""
class Solution(object):  
    def search(self, nums, target):  
        """ 
        :type nums: List[int] 
        :type target: int 
        :rtype: bool 
        """  
        left, right = 0, len(nums) - 1  
        while left <= right :  
            mid = (left+right) / 2  
            if nums[mid] == target : return True  
            # if nums[mid] == nums[left] : left += 1  #81题就多加了这一行，因为[1, 3, 1, 1, 1]这种case，这道题可加可不加
            elif nums[mid] > nums[left] :  
                if nums[mid] > target and nums[left] <= target :  
                    right = mid - 1  
                else : left = mid + 1  
            else :  
                if nums[mid] < target and nums[right] >= target :  
                    left = mid + 1  
                else : right = mid - 1  
        return False