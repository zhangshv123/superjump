class Solution:
	# @param nums: The integer array
	# @param target: Target number to find
	# @return the first position of target in nums, position start from 0 
	def binarySearch(self, nums, target): # find first index!
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
print s.binarySearch([1,2,2,5,5,7], 2) #如果找到了，就返回第一个出现的位置，这里2第一个出现在index = 1
#返回1
print s.binarySearch([1,2,2,5,5,7], 4)#如果没找到，就返回最后一个比4小的，和第一个比4大的
#返回（2，3）
print s.binarySearch([1,2,2,5,5,7], 8) #如果target比所有都大，就返回值不对
#返回（4，5），不对，所以要提前check target是不是比num里面最后一个大，就是比所有的都大

应该先问面试官，target会不会一定存在nums里面！！