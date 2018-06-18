#!/usr/bin/python

"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
双指针，一个指针 j 扫描数组，一个指针 i 记录没有重复数字的新数组的尾部。
(1) A[i]=A[j]，A[j]为重复数字，跳过。
(2) A[i]!=A[j]，将A[j]放到A[i+1]位置，i++
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

"""
lc80
Follow up for "Remove Duplicates":
    What if duplicates are allowed at most twice?

    For example,
    Given sorted array nums = [1,1,1,2,2,3],

    Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
    和I一样的思路，区别仅仅在于当A[end-1] = A[end] = A[i]时，A[i]为重复元素需跳过。
    而实际只需要比较A[end-1]和A[i]，因为当A[end-1] = A[i]时，根据sorted arry特性必然也有A[end]=A[end-1]。
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #end: idx of last ele no dup more than twice
        end = -1
        for i in range(len(nums)):
            if end < 1 or nums[i] != nums[end - 1]:
                end += 1
                nums[end] = nums[i]
        return end + 1