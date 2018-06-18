#!/usr/bin/python

class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        # write your code here
        left, right = 0, len(num) - 1
        while left < right:
            if num[left] < num[right]:
                return num[left]
            mid = left + (right - left) / 2
            if num[mid] >= num[left]:
                left = mid + 1
            else:
                right = mid 
        return num[left]