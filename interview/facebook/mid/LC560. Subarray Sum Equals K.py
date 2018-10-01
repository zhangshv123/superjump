"""
用一个哈希表来建立连续子数组之和跟其出现次数之间的映射，初始化要加入{0,1}这对映射，这是为啥呢，
因为我们的解题思路是遍历数组中的数字，用sum来记录到当前位置的累加和，我们建立哈希表的目的是为了
让我们可以快速的查找sum-k是否存在，即是否有连续子数组的和为sum-k，如果存在的话，那么和为k的子
组一定也存在，这样当sum刚好为k的时候，那么数组从起始到当前位置的这段子数组的和就是k，满足题意，
如果哈希表中实现没有m[0]项的话，这个符合题意的结果就无法累加到结果res中，这就是初始化的用途。
"""
from collections import defaultdict
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total, res, d = 0, 0, defaultdict(int)
        d[0] = 1 #代表和是0的有一种
        for num in nums:
            total += num
            res += d[total - k]
            d[total] += 1
        return res

linkedin follow up：
对于像[0...0]这样的array， res可能会非常大，所以return type可能是long不一定是int