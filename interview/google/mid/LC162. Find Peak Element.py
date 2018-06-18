"""
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
"""
#  一共只有4种情况，\         /       mid        \        /
#                  mid    mid      /   \        \     /
#                   \     /       /     \         mid
# 第一种肯定左边是峰值，
# 第二种肯定右边是峰值
# 第三种就是本身，return mid (line 32)
# 第四种往左往右都可以
class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, A):
        # write your code here
        start,end = 0,len(A)-1
        while start<end:
            mid = start + (end - start) /2
            if A[mid-1] > A[mid]:
                end = mid
            elif A[mid+1] > A[mid]:
                start = mid
            else:
                return mid
        
                