from sets import Set
class Solution(object):
	""
	使用set表来保存数组中的每一个数，每次遍历到一个数的时候看往上找到所有连续的数最多有几个，往下找比他小的数最多有几个．为了避免连续的序列中的数重复查找，在找到一个相邻的数之后就把他从hash表中删除，也就是一个连续的序列只会被查找一次．因此时间复杂度为O(n)．
	""
	def longestConsecutive(self, nums):
		res = 0
		set = Set()
		for num in nums:
			set.add(num)
		for num in nums:
			if num in set:
				cnt = 1
				pre = num-1
				set.remove(num)
				while pre in set:
					cnt+=1
					set.remove(pre)
					pre-=1
				suc = num+1
				while suc in set:
					cnt+=1
					set.remove(suc)
					suc+=1
			res = max(res,cnt)
		return res

s=Solution()
print s.longestConsecutive([-1,1,0])
			
			
		
