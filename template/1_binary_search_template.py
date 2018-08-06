class Solution:
	# @param nums: The integer array
	# @param target: Target number to find
	# @return the first position of target in nums, position start from 0 
	def binarySearch(self, nums, target):
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
		return start,end 
		
s = Solution()
print s.binarySearch([1,2,2,5,5,7], 4)
#返回（2，3）
print s.binarySearch([1,2,2,5,5,7], 8)
#返回（4，5），不对，所以要提前check target是不是比num里面最后一个大，就是比所有的都大