#!/usr/bin/python
"""
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
"""
"""
简单的说
    output[i] =  { i 前面的数的乘积}  X  { i 后面的数的乘积}
问题就解决了，首先从前往后扫描数组一遍，对每一个i，得到{i 前面的数的乘积}(可以称做output_before)，然后在从后往前扫描数组一遍，获得 { i 后面的数的乘积}(可以称做output_after)。 将两数相乘即为所求。
举个例子(如下图)，nums = {1,2,3,4}, 第一遍，从前往后扫描一遍，得到的output_before = {1, 1, 2, 6}. 从后往前扫描一遍，得到的output_after = {24, 12, 4, 1}.
那么  output [i] = output_before[i] * output_after[i],   output = {24, 12, 8, 6}
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output