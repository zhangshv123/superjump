class Solution:
	# @param nums: The integer array
	# @param target: Target number to find
	# @return the first position of target in nums, position start from 0 
	def binarySearch(self, nums, target):
		start, end = 0, len(nums)
#		相邻就退出循环
#       start = 1, end = 2 就退出循环 
		while start + 1 < end :
			mid = (start + end) / 2
			if nums[mid] < target :
				#start = mid + 1 也是对的,但是费脑子,不要费脑子！
				start = mid
			else :
				#end = mid - 1 也是对的,但是费脑子,不要费脑子！
				end = mid
				
#		double check		
		if nums[start] == target :
			return start
		elif nums[end] == target :
			return end
		return -1;

s = Solution()
print s.binarySearch([2,2], 2)