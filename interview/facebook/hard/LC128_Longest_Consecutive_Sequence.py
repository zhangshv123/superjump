"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""
"""
这道题要求求最长连续序列，并给定了O(n)复杂度限制，我们的思路是，使用一个集合set存入所有的数字，
然后遍历数组中的每个数字，如果其在集合中存在，那么将其移除，然后分别用两个变量pre和next算出其前一个数跟后一个数，
然后在集合中循环查找，如果pre在集合中，那么将pre移除集合，然后pre再自减1，直至pre不在集合之中，
对next采用同样的方法，那么next-pre-1就是当前数字的最长连续序列，更新res即可
"""
import sets
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        res = 0
        for num in nums:
            if num not in s:
                continue
            prev, next = num - 1, num + 1
            while prev in s:
                s.remove(prev)
                prev -= 1
            while next in s:
                s.remove(next)
                next += 1
            res = max(res, next - prev - 1)
        return res

"""
我们也可以采用哈希表来做，刚开始哈希表为空，然后遍历所有数字，如果该数字不在哈希表中，那么我们分别看其左右两个数字
是否在哈希表中，如果在，则返回其哈希表中映射值，若不在，则返回0，然后我们将left+right+1作为当前数字的映射，
并更新res结果，然后更新d-left和d-right的映射值
"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length_map = {}
        max_length = 0
        for num in nums:
            if num not in length_map:
                left = 0 if num - 1 not in length_map else length_map[num - 1]
                right = 0 if num + 1 not in length_map else length_map[num + 1]
                length = left + 1 + right
                length_map[num] = length
                max_length = max(max_length, length)
                length_map[num - left] = length
                length_map[num + right] = length
        return max_length