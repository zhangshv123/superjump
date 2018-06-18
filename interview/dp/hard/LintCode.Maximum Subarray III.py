"""
Given an array of integers and a number k, find k non-overlapping subarrays which have the largest sum.

The number in each subarray should be contiguous.

Return the largest sum.
Example
Given [-1,4,-2,3,-2,3], k=2, return 8
"""
class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def maxSubArray(self, nums, k):
        # write your code here
        sums = [0]
        for num in nums:
            sums.append(sums[-1] + num)
        print sums
        n = len(nums)
        dp = [[-sys.maxint for _ in range(k + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(k + 1):
                if i == 0 and j == 0:
                    dp[i][j] = 0     
                elif i == 0 and j <= k:
                    dp[i][j] = -sys.maxint
                elif j == 0 and i <= n: 
                    dp[i][j] = 0
                else:
                    #不用最后一个元素
                    dp[i][j] = dp[i - 1][j]
                    #用最后一个元素
                    for l in range(i):
                        dp[i][j] = max(dp[i][j], dp[l][j - 1] + sums[i] - sums[l])
        return dp[n][k]