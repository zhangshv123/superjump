思路：先排序，假设 a < b < c，然后看花花视频的思路 greedy
https://www.youtube.com/watch?v=bojX9bdra-w
时间复杂度：O(n^2)
class Solution(object):
	def triangleNumber(self, nums):
		if len(nums) < 3:
			return 0
		nums = sorted(nums)
		res = 0
		for right in range(len(nums)-1, 1, -1):
			mid = right -1
			left = 0
			while left < mid:
				while self.isValid(left, mid, right, nums):
					res += mid - left
					mid -= 1
				left += 1
		return res
			
	def isValid(self, left, mid, right, nums):
		if left >= 0 and mid >= left and right < len(nums):
			a = nums[left]
			b = nums[mid]
			c = nums[right]
			return a + b > c and a + c > b and b + c > a
		return False

s = Solution()
print s.triangleNumber([2,2,3,4])
print s.triangleNumber([1,1,1,1])
				
		