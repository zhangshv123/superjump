思路：python没有treemap的数据结构, orderedDict只是保证key是按照inser顺序存在
时间复杂度： insert O(logn), getCover: O(n)
import collections
class Solution(object):
	od = dict()
	def addInterval(self, start_time, end_time):
		if start_time not in self.od:
			self.od[start_time] = 1 
		else:
			self.od[start_time] += 1  #如果是start ,value就+1
		
		if end_time not in self.od:
			self.od[end_time] = -1 
		else:
			self.od[end_time] -= 1    #如果是end ,value就-1
	
	def getTotalCoverageLength(self):
		start_idx = -1 #这样我们需要结算的时候就知道从哪里开始的
		depth = 0 #模拟stack，当stack的size是0的时候，我们就开始结算了
		res = 0
		sod = collections.OrderedDict(sorted(self.od.items())) #按照key来排序
		for key in sod.keys():
			depth += sod[key]
			if sod[key] > 0:
				if start_idx == -1:
					start_idx = key
			else:
				if depth == 0:
					res += key - start_idx
					start_idx = -1
		return res

s = Solution()
s.addInterval(3, 6)
s.addInterval(8, 9)
s.addInterval(1, 5)
print s.getTotalCoverageLength()
					
			
		
		
		
					
	
