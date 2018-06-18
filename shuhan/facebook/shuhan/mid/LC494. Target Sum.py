#!/usr/bin/python
class Solution(object):
	def findTargetSumWays(self, nums, S):
		dp = [{} for _ in range(len(nums))]
		return self.helper(nums, S, 0, dp)
		
	def helper(self,nums, S, index, dp):
		if index >= len(nums):
			return 1 if S == 0 else 0
		if S in dp[index]:
		    return dp[index][S]
		add = self.helper(nums,S+nums[index],index+1, dp)
		minus = self.helper(nums,S-nums[index],index+1, dp)
		dp[index][S] = add + minus
		return add + minus
        

S = Solution()
print(S.findTargetSumWays([1,1,1,1,1],3))