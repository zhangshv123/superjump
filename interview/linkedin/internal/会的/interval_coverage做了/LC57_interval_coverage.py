思路：python没有treemap的数据结构, orderedDict只是保证key是按照inser顺序存在
时间复杂度： insert O(logn), getCover: O(n)
from collections import OrderedDict
class Solution(object):
	od = OrderedDict()
	def addInterval(self, start_time, end_time):
		if start_time not in self.od:
			self.od[start_time] = 1 
		else:
			self.od[start_time] += 1 #如果是start ,value就+1
		
		if end_time not in self.od:
			self.od[end_time] = -1 
		else:
			self.od[end_time] -= 1 #如果是end ,value就-1
	
	def getTotalCoverageLength(self):
		start_idx = -1 #这样我们需要结算的时候就知道从哪里开始的
		depth = 0 #模拟stack，当stack的size是0的时候，我们就开始结算了
		res = 0
		for key in self.od.keys():
			depth += self.od[key]
			if self.od[key] > 0:
				if start_idx == -1:
					start_idx = key
			else:
				if depth == 0:
					res += key - start_idx
					start_idx = -1
		return res

s = Solution()
s.addInterval(1, 3)
s.addInterval(3, 4)
print s.getTotalCoverageLength()
					
			
		
		
		
					
	
