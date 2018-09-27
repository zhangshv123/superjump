#longest increasing subsequence:
#	最长递增子序列(子序列不一定要连续,num不会有duplicate)
#	index 0  1  2  3  4  5  6
#	value 3  2  1  5  2  3  7
#
#	返回长度，比如上面这个就是[1,2,3,7]返回4
#
#	解法一：naive O(n^2)
#	dp[]: 
#   以index为0为结尾的最长递增子序列的长度是1
#	dp[0] = 1
#
#
#	解法二：binary search O(nlogn)
#	dp[]:长度为1的递增子序列的最小尾数是1
#	dp[1] = 1
#	递推方程：
#	given k
#	 find i: 
#	 1)dp[i]< k <= dp[i+1]
#	 	dp[i+1] = k
#	 2)dp[n-1] < k
#	 	dp.append(k)
	
from collections import defaultdict
class Solution(object):
	def lengthOfLIS(self, nums):
		if not nums or len(nums) == 0:
			return 0
		dp = []
		dp.append(-1)
		dp.append(nums[0])
		for num in nums:
			i = self.bs(dp,num)
			if dp[-1] < num:
				dp.append(num)
			elif dp[i] < num <= dp[i+1]:
				dp[i+1] = num
		return len(dp)-1
	
	def bs(self, nums, target):#返回比自己小的最后位置[1,2,2,4,5]找3，会返回2,如果找到了，就返回第一个位置，比如找2，返回1
		if len(nums) == 0:
			return -1
			
		start, end = 0, len(nums) - 1
		while start + 1 < end:
			mid = (start + end) / 2
			if nums[mid] < target:
				start = mid
			else:
				end = mid
				
		if nums[start] == target:
			return start
		if nums[end] == target:
			return end
		return start
		
				
s = Solution()
print s.lengthOfLIS([10,9,2,5,3,7,101,18])
