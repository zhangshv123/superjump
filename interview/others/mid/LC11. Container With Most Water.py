"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""
"""
思路：

由于ai和aj (i<j) 组成的container的面积：S(i,j) = min(ai, aj) * (j-i)

所以对于任何S(i'>=i, j'<=j) >= S(i,j)，由于j'-i' <= j-i，必然要有min(ai',aj')>=min(ai,aj)才行。同样可以采用头尾双指针向中间移动：

当a(left) < a(right)时，对任何j<right来说

(1) min(a(left),aj) <= a(left) = min(a(left), a(right))
(2) j-left < right-left

所以S(left, right) > S(left, j<right)。排除了所有以left为左边界的组合，因此需要右移left。同理，当a(left) > a(right)时，需要左移right。而当a(left) = a(right)时，需要同时移动left和right。

思路整理：
left = 0, right = n-1
(1) a[left] < a[right], left++
(2) a[left] > a[right], right--
(3) a[left] = a[right], left++, right--
终止条件：left>-right
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        res = 0
        while left < right:
            res = max(res, (right - left) * min(height[left], height[right]))
            if height[right] < height[left]:
                right -= 1
            elif height[right] > height[left]:
                left += 1
            else:
                right -= 1
                left += 1
        return res