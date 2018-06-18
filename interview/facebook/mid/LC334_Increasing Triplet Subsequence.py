#!/usr/bin/python
"""
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k 
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.
"""
"""
todo: top solution, time complexity and O(1) space complexity.
"""
"""
不断的缩小x1和x2，看看是否有第三个数比x2大.如果出现第三个数 n> x2，则之前必定还有个数x 小于x2，就是说满足 x < x2 < n
但是题目中要求我们O(n)的时间复杂度和O(1)的空间复杂度
我们下面来看满足题意的方法，这个思路是，我们遍历数组，维护一个最小值，和倒数第二小值，遍历原数组的时候，
如果当前数字小于等于最小值，更新最小值，如果小于等于倒数第二小值，更新倒数第二小值，如果当前数字比最小值
和倒数第二小值都大，说明此时有三个递增的子序列了，直接返回ture，否则遍历结束返回false，参见代码如下：
"""
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        small, big = sys.maxint, sys.maxint
        for num in nums:
            if num <= small:
                small = num
            elif num <= big:
                big = num
            else:
                return True
        return False



"""
space complexity O(n), not qualify
"""
class Solution(object):
        def increasingTriplet(self, nums):
            """
            :type nums: List[int]
            :rtype: bool
            """
            if len(nums) < 3:
                return False
            # record whether smaller element in the left
            left = [False for _ in range(len(nums))]
            min_left = nums[0]
            for i in range(1, len(nums)):
                left[i] = nums[i] > min_left
                min_left = min(min_left, nums[i])
            max_left = nums[-1]
            # check whether larger ele in the right
            for i in reversed(range(1, len(nums) - 1)):
                if left[i] and nums[i] < max_left:
                    print i, nums[i], max_left
                    return True
                max_left = max(max_left, nums[i])
            return False