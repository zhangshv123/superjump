"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
"""
#这是不改变相对顺序的
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #end: last ele that not equal 0
        end = -1
        for i in range(len(nums)):
            if nums[i] != 0:
                end += 1
                nums[end], nums[i] = nums[i], nums[end]
            
#如果改变相对顺序 2个指针 参见wayfair的面经,移动次数最少！(重点)
class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    def moveZeroes(self, nums):
        i,j=0,len(nums)-1
        while i<=j:
            while i<=j and nums[i] != 0:
                i+=1
            while i<=j and nums[j] == 0:
                j-=1
            if i<=j:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
        return nums

class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    def partitionArray2(self, nums):
        i,j=0,len(nums)-1
        while i<=j:
            while i<=j and nums[i]<0:
                i+=1
            while i<=j and nums[j]>=0:
                j-=1
            if i<=j:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
        return nums
            
s = Solution()      
numbers=[1,-2,3,-1,2,-3]
print s.partitionArray2(numbers)
