#正常的二分法
def bs(nums, target):
	start = 0
	end = len(nums) - 1 
	while start <= end:
		mid = (start + end) / 2
		if target == nums[mid]:
			return mid
		elif target < nums[mid]:
			end = mid - 1
		else:
			start = mid + 1	
	return -1

# return the iterator of the first value that is not less than the target
#lower_bound是返回第一个大于等于的
def lower_bound(nums, target):
	start = 0
	end = len(nums) - 1
	while start <= end:#为了卡住一个数
		mid = (start + end) / 2
		if nums[mid] < target:
			start = mid + 1
		else:
			end = mid - 1
	return start
#upper_bound是返回第一个大于的
def upper_bound(nums, target):
	start = 0
	end = len(nums) - 1
	while start <= end:
		mid = (start + end) / 2
		if nums[mid] <= target:
			start = mid + 1
		else:
			end = mid - 1
	return start
s = [5,7,7,8,8,10]
print lower_bound(s, 8)
print upper_bound(s, 8)