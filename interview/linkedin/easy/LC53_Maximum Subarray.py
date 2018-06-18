"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""
"""
所有求substring，subarray， 最大最小都转化为以i为结尾的最大最小，
然后对于所有以i为最大最小的出的结论里遍历得到原问题的最大最小
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = maxEndingHere = nums[0]
        for num in nums[1:]:
            maxEndingHere = max(maxEndingHere + num, num)
            maxSum = max(maxEndingHere, maxSum)
        return maxSum

#另外一种
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        nums.insert(0,0)#加一个dummy node
        total = nums[0]
        small = nums[0]
        for i in range(1,len(nums)):
            total += nums[i]
            res = max(res,total - small)
            small = min(small,total)
        return res