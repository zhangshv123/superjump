"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
"""
#dp
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [sys.maxint for _ in range(n)]
        dp[0] = 0
        for i in range(n):
            for j in range(i + 1, min(i + nums[i] + 1, n)):
                dp[j] = min(dp[j], dp[i] + 1)
        return dp[n - 1]

#bfs去重扫层
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) < 2:
            return 0
        q = []
        q.append(0)
        idx, level, n = 0, 0, len(nums)
        while idx < len(q):
            size = len(q)
            level += 1
            while idx < size:
                pos= q[idx]
                idx += 1
                if pos + nums[pos] >= n - 1:
                    return level
                for i in range(pos + 1, min(pos + nums[pos] + 1, n)):
                    if i in q:
                        continue
                    q.append(i)      