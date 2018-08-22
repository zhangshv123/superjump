思路: 遍历一遍数组, 如果是奇数位置并且其值比下一个大,则交换其值, 如果是偶数位置并且其值比下一个小, 则交换其值. 时间复杂度是O(N)
class Solution(object):
	def wiggleSort(self, nums):
		for i in range(len(nums)-1):
			if i%2 == 0 and nums[i] > nums[i+1]:
				nums[i], nums[i+1] = nums[i+1], nums[i]
			elif i%2 == 1 and nums[i] < nums[i+1]:
				nums[i], nums[i+1] = nums[i+1], nums[i]
		return nums

s = Solution()
print s.wiggleSort([3,5,2,1,6,4])
				
		