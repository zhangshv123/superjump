#!/usr/bin/python
"""
Trapping Rain Water
"""

"""
easy to understand
对任意位置i，在i上的积水，由左右两边最高的bar：A[left] = max{A[j], j<i}, 
A[right] = max{A[j], j>i}决定。定义Hmin = min(A[left], A[right])，则积水量Si为：

Hmin <= A[i]时，Si = 0
Hmin > A[i]时，Si = Hmin - A[i]
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftBars = [0 for _ in range(len(height))]
        rightBars = [0 for _ in range(len(height))]
        for i in range(1, len(height)):
            leftBars[i] = max(leftBars[i - 1], height[i - 1])
        trap_water = 0
        for i in reversed(range(len(height) - 1)):
            rightBars[i] = max(rightBars[i + 1], height[i + 1])
            minBar = min(leftBars[i], rightBars[i])
            if minBar > height[i]:
                trap_water += minBar - height[i]
        return trap_water




class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height is None or len(height) < 3:
            return 0
        num = len(height)
        left_bar, right_bar = height[0], height[num - 1]
        left, right = 0, num - 1
        water_trapped = 0
        while left < right:
            if left_bar < right_bar:
                left += 1
                left_bar = max(left_bar, height[left])
                water_trapped += left_bar - height[left]
            else:
                right -= 1
                right_bar = max(right_bar, height[right])
                water_trapped += right_bar - height[right]
        return water_trapped

class Solution:
    # @param heights: a list of integers
    # @return: a integer
    def trapRainWater(self, heights):
        n = len(heights)
        l, r, water, minHeight = 0, n - 1, 0, 0
        while l < r:
            while l < r and heights[l] <= minHeight:
                water += minHeight - heights[l]
                l += 1
            while l < r and heights[r] <= minHeight:
                water += minHeight - heights[r]
                r -= 1
            minHeight = min(heights[l], heights[r])
        return water

