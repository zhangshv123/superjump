"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

原题是用一个hashmap，扫一遍nums1和nums2的数组，O(T) = m+n
如果差不多长度，也可以用2个指针(重复数字可以cover)

followup:
    1.What if the given array is already sorted? How would you optimize your algorithm?
    一开始我说可以通过binary search找lower bound和upper bound，就知道这个数出现多少次，然后把交集加进去，
    然后面试官提醒问说需要搜两次吗，后来答搜一次，binary search找到lower bound，就是这个数字第一个出现的位置，
    然后可以通过这个位置linear search往后找这个数字重复的次数
    O(T) = O(mlogn)
    
    2.What if nums1's size is small compared to nums2's size? Which algorithm is better?
    二分查找的更好
    
    3.What if elements of nums2 are stored on disk, and the memory is limited such that you cannot 
    load all elements into the memory at once?
    If only nums2 cannot fit in memory, put all elements of nums1 into a HashMap, read chunks of array 
    that fit into the memory, and record the intersections.

    If both nums1 and nums2 are so huge that neither fit into the memory, sort them individually 
    (external sort), then read 2 elements from each array at a time in memory, record intersections.
    
"""
from collections import defaultdict
class Solution(object):
    #这种做法基于2个差不多长度
    def intersect(self, nums1, nums2):
        i, j, res = 0, 0, []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
        return res
    #这种做法基于其中一个很长        
    # 就用二分法在长的里面查找短的数字
    # 具体可见
    # https://www.geeksforgeeks.org/union-and-intersection-of-two-sorted-arrays-2/
s = Solution()
print s.intersect([1], [1,1,2,4])