"""
Start from its last element, traverse backward to find the first one with index i that satisfy num[i-1] < num[i]. 
So, elements from num[i] to num[n-1] is reversely sorted.
To find the next permutation, we have to swap some numbers at different positions, to minimize the increased amount, 
we have to make the highest changed position as high as possible. Notice that index larger than or equal to i is not 
possible as num[i,n-1] is reversely sorted. So, we want to increase the number at index i-1, clearly, swap it with the 
smallest number between num[i,n-1] that is larger than num[i-1]. For example, original number is 121543321, we want to 
swap the ‘1’ at position 2 with ‘2’ at position 7.
The last step is to make the remaining higher position part as small as possible, we just have to reversely sort the 
num[i,n-1]
"""

"""
Reverse find first number which breaks descending order.

Exchange this number with the least number that’s greater than this number.

Reverse sort the numbers after the exchanged number.

"""
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1
        if i < 0:
            nums.reverse()
            return
        l = -1
        for j in reversed(range(i, len(nums))):
            if nums[j] > nums[i]:
                l = j
                break
        nums[i], nums[l] = nums[l], nums[i]
        nums[i + 1:] = sorted(nums[i + 1:])
    def prevPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0:
            if nums[i] > nums[i + 1]:
                break
            i -= 1
        if i < 0:
            nums.reverse()
            return
        l = -1
        for j in reversed(range(i, len(nums))):
            if nums[j] < nums[i]:
                l = j
                break
        nums[i], nums[l] = nums[l], nums[i]
        nums[i + 1:] = reversed(sorted(nums[i + 1:]))