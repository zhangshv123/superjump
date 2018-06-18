"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].
"""
from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        h = []
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1
        for val, freq in freqs.items():
            if len(h) < k:
                heapq.heappush(h, (freq, val))
            else:
                if h[0][0] < freq:
                    heapq.heapreplace(h, (freq, val))
        return map(lambda a: a[1], h)