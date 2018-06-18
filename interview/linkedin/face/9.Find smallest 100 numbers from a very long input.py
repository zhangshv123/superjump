import heapq
class Solution(object):
    def closestKPoint(self,nums, k):
        h = []
        for num in nums:
            if len(h) < k:
                heapq.heappush(h, num)
            else:
                if h[-1] > num:
                    heapq.heapreplace(h, num)
        return h
s = Solution()
print s.closestKPoint([1,2,3], 2)