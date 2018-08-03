class Solution(object):
	def exclusiveTime(self, n, logs):
		"""
		:type n: int
		:type logs: List[str]
		:rtype: List[int]
		"""
		res = [0] * n
		stk = []
		for log in logs:
			fid,start_end,time = log.split(":")
			fid, time = int(fid), int(time)
			if start_end == "start":
				if len(stk) > 0:
					res[stk[-1][0]] += time - stk[-1][1]
				stk.append((fid,time))
			elif start_end == "end":
				cur = stk.pop()
				res[cur[0]] += time - cur[1] + 1
				if len(stk) > 0:
					stk[-1] = (stk[-1][0],time + 1)
		return res

s = Solution()
print s.exclusiveTime(2, ["0:start:0",
 "1:start:2",
 "1:end:5",
 "0:end:6"])
				
				
				
			
			