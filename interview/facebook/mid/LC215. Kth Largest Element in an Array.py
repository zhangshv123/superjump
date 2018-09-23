"""
O(nlogk) running time + O(k) memory
在数字集合中寻找第k大，可以考虑用Max Heap，将数组遍历一遍，加入到一个容量为k的PriorityQueue，最后poll() k-1次，
那么最后剩下在堆顶的就是kth largest的数字了。
"""
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        h = []
        for i in range(len(nums)):
            if i < k:
                heapq.heappush(h, nums[i])
            else:
                if h[0] < nums[i]:
                    heapq.heapreplace(h, nums[i])
        return h[0]

"""
Time Complexity: average = O(n); worst case O(n^2), O(1) space
注意事项：
partition的主要思想：将比pivot小的元素放到pivot左边，比pivot大的放到pivot右边
pivot的选取决定了partition所得结果的效率，可以选择left pointer，更好的选择是在left和right范围内随机生成一个；

"""
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k = len(nums) - k
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            i, j = lo, hi + 1
            while True:
                i += 1
                j -= 1
                while i < hi and nums[i] < nums[lo]:
                    i += 1
                while j > lo and nums[lo] < nums[j]:
                    j -= 1
                if i >= j:
                    break
                nums[i], nums[j] = nums[j], nums[i]
            nums[lo], nums[j] = nums[j], nums[lo]
            if j < k:
                lo = j + 1
            elif j > k:
                hi = j - 1
            else:
                break
        return nums[k]       