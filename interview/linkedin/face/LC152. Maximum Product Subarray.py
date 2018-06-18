"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        g = h = 1
        res = -sys.maxint
        for num in nums:
            g, h = max(g * num, h * num, num),  min(g * num, h * num, num)
            res = max(res, g)
        return res
