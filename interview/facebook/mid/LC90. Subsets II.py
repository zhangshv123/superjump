from collections import defaultdict
class Solution(object):
	def subsetsWithDup(self, nums):
		res = []
		total = []
		d = defaultdict(int) #存每个数字出现了几次 d = {1:1, 2:2, 3:1}
		arr = [] #存有哪些数字，比如这里 arr= [1,2]
		
		for num in nums:
			if num not in d:
				arr.append(num)
			d[num] += 1
		
		self.dfs(nums, 0, res, [], d, arr)
		for path in res:
			tep = []
			for i in range(len(path)):
				for j in range(path[i]):
					tep.append(arr[i])
			total.append(tep[:])
		return total
					
	def dfs(self, nums, idx, res, path, d, arr):
		if idx == len(d):
			res.append(path[:])
			return
		
		for pos in range(d[arr[idx]]+1):
			path.append(pos)
			self.dfs(nums, idx+1, res, path, d, arr)
			path.pop()
s = Solution()
print s.subsetsWithDup([1,2,2,3])
