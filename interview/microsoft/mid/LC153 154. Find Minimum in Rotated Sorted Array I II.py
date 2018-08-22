"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
"""
"""
1. nums[mid] = nums[right], 说明找到了要找的答案.

2. nums[mid] < nums[right]，这种情况是当前的数小于右边数组的一个数，说明当前的位置肯定是在右半数组中，因此可以往左查找[left, mid]

3. nums[mid] > nums[right]，这种情况是当前的数大于右边数组的一个数，说明当前的位置在左半数组中，因此要查找右半数组第一个数的位置可以向右搜索[mid+1, right]
"""
参考：
http://bangbingsyb.blogspot.com/2014/11/leecode-find-minimum-in-rotated-sorted.html
class Solution(object):
	def findMin(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		left,right = 0,len(nums)-1
		mid = 0
		while left <= right:
			mid = left + (right - left)/2
			if nums[mid] == nums[right]:
			   return nums[mid]
			elif nums[mid] < nums[right]:
				right = mid
			else:
				left = mid+1
	   
		return nums[left]
"""
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
"""
class Solution(object):
	    def findMin(self, nums):
			"""
			:type nums: List[int]
			:rtype: int
			"""
			left,right = 0,len(nums)-1
			mid = 0
			while left <= right:
				mid = left + (right - left)/2
				if nums[mid] == nums[right]:
				   right -= 1
				"""
				nums[mid] = nums[right]，这种情况下无法判断当前位置是在左边还是右边，但是让右指针左移一位并不会影响到最小值，
				为nums[mid] = nums[right], 因此搜索[left, right-1]
				"""
				elif nums[mid] < nums[right]:
					right = mid
				else:
					left = mid+1
		   
			return nums[left]		