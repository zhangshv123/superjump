#!/usr/bin/python
"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. 
It doesn't matter what you leave beyond the new length.
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #end: idx of last ele not dup
        end = -1
        for i in range(len(nums)):
            if end < 0 or nums[i] != nums[end]:
                end += 1
                nums[end] = nums[i]
        return end + 1
s = Solution()
nums = [1,1,2,2,2,3]
print nums[:s.removeDuplicates(nums)]