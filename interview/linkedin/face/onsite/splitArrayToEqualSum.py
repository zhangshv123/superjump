#!/usr/bin/python
class Solution:
	# @param {integer[]} nums
	# @return {integer[]}
	def canSplit(self,arr,k):
		arr.sort()
		n = len(arr)
		if k == 1:
			return True
		tot = sum(arr)
		if n < k or tot%k != 0:
			return False
		subSum = tot/k
		used = [False for _ in range(n)]
		path = []
		res = []
		return self.helper(arr,k,path,res,used,subSum)
			
	def helper(self,arr,k,path,res,used,subSum):
		if sum(path) == subSum:
			print subSum,path
			res.append(path)
			if len(res) == k and all(item == True for item in used):
				return True
		elif sum(path) > subSum:
			return False
		
		for i in range(len(arr)):
			if used[i] == False:
				path.append(arr[i])
				used[i] == True
				self.helper(arr,k,path,res,used,subSum)
				used[i] == False
				path.pop()
			
s = Solution()
print s.canSplit([2,1,4, 5, 3, 3],3)

	