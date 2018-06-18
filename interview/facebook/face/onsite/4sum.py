"""
3. 4sum -- O(n^3) 跟 O(n^2) 最後要求只用兩個for loop當有一個a+b+c+d = target就return
The idea is: use hashmaps to cache all the visited pair sum. We maintain two hashmaps: sum2index2cnt 
is to cache the sum and index frequency in pairs to make the sum; sum2paircnt is to store how many pairs 
can make that sum. NOTE here, j could appear in the previous visited pairs to make -sum, which is not valid.
 So we need to make sure there is a previous pair of -sum that does not contain j index. 
 sum2index2cnt[-sum][j] != sum2paircnt[-sum] can do it in O(1).
"""
#要求是只要知道一个答案就返回!不要求所有答案！
from collections import defaultdict
class Solution(object):
	def fourSum(self, nums, target):
		d = defaultdict(list)
		for i in range(len(nums)):
			for j in range(i + 1,len(nums)):
				twoSum = nums[i] + nums[j]
				if target - twoSum in d:
					for pi, pj in d[target - twoSum]:
						if pi != i and pj != j and pj != i and pj != j:
							return True
				d[twoSum].append((i, j))
		return False
s = Solution()
print s.fourSum([1,2,3,4,5,6], 13)
				

from collections import defaultdict
class Solution(object):
	def fourSum(self, nums, target):
		nums.sort()
		d = defaultdict(int)
		dd = [defaultdict(int) for _ in range(len(nums))]
		for i in range(len(nums)):
			for j in range(len(nums)):
				twoSum = nums[i] + nums[j]
				if target - twoSum in d:
					# if j does not appear in every pair
					if d[target - twoSum] != dd[j][target - twoSum]:
						return True
				dd[i][twoSum] += 1
				dd[j][twoSum] += 1
				d[twoSum] += 1
		return False
s = Solution()
print s.fourSum([1,2,3,4,5,6], 22)

#2个指针做法：
from collections import defaultdict
class Solution(object):
	def fourSum(self, nums, target):
		res = []
		nums.sort()
		s = set()#为了避免重复
		for i in range(0,len(nums) -3):
			for j in range(i+1,len(nums)-2):
				left,right = j+1,len(nums)-1
				while left < right:
					total = nums[i]+nums[j]+nums[left]+nums[right]
					if total == target:
						if (nums[i],nums[j],nums[left],nums[right]) not in s:
							res.append((nums[i],nums[j],nums[left],nums[right]))
							s.add((nums[i],nums[j],nums[left],nums[right]))
						left += 1
						right -= 1
					elif total < target:
						left += 1
					else:
						right -= 1
		return res
s = Solution()
print s.fourSum([1,2,3,4,5,6], 13)